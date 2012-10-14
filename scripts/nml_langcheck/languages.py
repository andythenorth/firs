"""
License:
    nml_langcheck is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    nml_langcheck is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""
import re, codecs, subprocess

report_number = 1 # Unique number for string reports.


class LanguageReadError(Exception):
    """
    Exception for falling out of a language loading process in case loading fails.
    """
    def __init__(self, err):
        self.err = err
    def __str__(self):
        text = "LanguageReadError(%r)" % self.err
        return text.encode('ascii')


def make_revline(rev, line):
    if rev is None:
        if line is None: return None
        return u"Line %d" % line
    else:
        if line is None:
            return u"r%d" % rev
        return "at line %d, r%d" % (line, rev)


class StringReport(object):
    """
    Report about 'bad' strings.

    @ivar report_id: Unique number for this report.
    @type report_id: C{int}

    @ivar str_name: Name of the string.
    @type str_name: C{unicode}

    @ivar trans_text: Current translation text (if available).
    @type trans_text: C{unicode} or C{None}

    @ivar trans_line: Line number in the translation (if available).
    @type trans_line: C{int} or C{Non}

    @ivar trans_rev: Revision number of the current translation text (if
                     available).
    @type trans_rev: C{int} or C{None}

    @ivar master_text: Current master text (if available).
    @type master_text: C{unicode} or C{None}

    @ivar master_line: Line number in the master file (if available).
    @type master_line: C{int} or C{None}

    @ivar master_rev: Revision number of the current master text (if
                      available).
    @type master_rev: C{int} or C{None}

    @ivar old_text: Master text at creation time of the current translation
                    (if available).
    @type old_text: C{unicode} or C{None}

    @type old_rev: Revision of the master text at creation time of the current
                   translation (if available).
    @type old_rev: C{int} or C{None}
    """
    def __init__(self, str_name):
        global report_number
        self.report_id = report_number
        report_number = report_number + 1

        self.str_name = str_name
        self.trans_text = None
        self.trans_line = None
        self.trans_rev = None
        self.master_text = None
        self.master_line = None
        self.master_rev = None
        self.old_text = None
        self.old_rev = None

    def write(self, fp):
        text = [u'%s:\n' % (self.str_name,)]
        printed = False

        if self.trans_text is not None:
            if printed: text.append(u'\n')
            rv = make_revline(self.trans_rev, self.trans_line)
            if rv is None:
                text.append(u'\tTranslation: "%s"\n' % self.trans_text)
            else:
                text.append(u'\tTranslation %s: "%s"\n' % (rv, self.trans_text))
            printed = True

        if self.master_text is not None:
            if printed: text.append(u'\n')
            rv = make_revline(self.master_rev, self.master_line)
            if rv is None:
                text.append(u'\tCurrent source: "%s"\n' % self.master_text)
            else:
                text.append(u'\tCurrent source %s: "%s"\n' % (rv, self.master_text))
            printed = True

        if self.old_text is not None:
            if printed: text.append(u'\n')
            rv = make_revline(self.old_rev, None)
            if rv is None:
                text.append(u'\tOld source: "%s"\n' % self.old_text)
            else:
                text.append(u'\tOld source %s: "%s"\n' % (rv, self.old_text))
            printed = True


        for line in text:
            fp.write(line.encode('utf-8'))


class StringDefintion(object):
    """
    Data of a string entry in a language file.

    @ivar name: Name of the string.
    @type name: C{unicode}

    @ivar gender: Optional gender of the string.
    @type gender: C{unicode} or C{None}

    @ivar number: Line number in the file.
    @type number: C{int}

    @ivar text: Text of the string.
    @type text: C{unicode}

    @ivar rev: Revision of the string if available.
    @type rev: C{int} or C{None}
    """
    def __init__(self, name):
        self.name = name
        self.gender = None
        self.number = None
        self.text = None
        self.rev = None

    def get_name(self):
        """
        Return the name of the string (extended with gender, if available).

        @return: Name of the string.
        @rtype:  C{unicode}
        """
        if self.gender is None: return self.name
        return self.name + u"." + self.gender


# Pattern to match annotation revision.
re_annot = re.compile(u' *(\\d+):')
utf8_bom = codecs.BOM_UTF8.decode('utf-8')

def get_annotated(fname, revision):
    """
    Get the lines of the file, annotated with revision numbers.

    @param fname: Filename to load.
    @type  fname: C{str}

    @param revision: Revision to query.
    @type  revision: C{int} or C{None}

    @return: Iterator returning tuples (revision, line number, line)
    @rtype:  C{iter} yielding tuples (C{int}, C{int}, C{unicode})
    """
    cmd = ['hg', 'annotate']
    if revision is not None: cmd.extend(['-r', str(revision)])
    cmd.append(fname)

    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out_data, err_data = p.communicate()
    if err_data != "":
        msg= u'Warning: Mercurial command \"%s\" failed (message: "%s")' \
            % (u" ".join(cmd), err_data)
        raise LanguageReadError(msg)

    out_data = out_data.decode('utf-8')
    for idx, line in enumerate(out_data.split(u'\n')):
        if idx == 0 and line[0] == utf8_bom: line = line[1:]
        line = line.rstrip()
        m = re_annot.match(line)
        if m:
            i = m.end()
            if len(line) > i and line[i] == ' ': i = i + 1
            if idx == 0  and len(line) > i and line[i] == utf8_bom: i = i + 1

            if len(line) == i:
                yield int(m.group(1)), idx + 1, u''
            else:
                yield int(m.group(1)), idx + 1, line[i:]


def read_lang(fname, revision):
    """
    Read the language file, and returns its strings, and the last changed revision.

    @param fname: Filename to load.
    @type  fname: C{str}

    @param revision: Revision to query.
    @type  revision: C{int} or C{None}

    @return: Sequence of read language strings.
    @rtype:  C{list} of L{StringDefintion}

    @note: Throws a L{LanguageReadError} exception in case retrieval fails.

    @todo: Handle cases
    """
    line_numbers = {} # Temporary mapping of STR to line number.
    texts = []
    for rev, num, text in get_annotated(fname, revision):
        # cases!!
        if len(text) == 0 or text[0] == u'#': continue

        i, j = text.find(u' '), text.find(u'\t')
        if i < 0:
            es = j
        elif j < 0:
            es = i
        else:
            es = min([i, j])

        if es < 0:
            raise LanguageReadError(u"Invalid string-name at line %d in %r (text %r)"
                    % (num, fname, text))
        j = text.find(u'.')
        if j > 0 and j < es:
            name, gender = text[:j], text[j + 1:es]
        else:
            name, gender = text[:es], None

        i = text.find(u':')
        if i < 0:
            raise LanguageReadError(u"Missing colon at line %d in %r (text %r)"
                    % (num, fname, text))

        text = text[i + 1:]
        tid = (name, gender)

        if tid in line_numbers:
            raise LanguageReadError(u"String %r is defined twice in %r (at lines %d and %d)"
                    % (name, fname, line_numbers[name], num))

        line_numbers[tid] = num
        sd = StringDefintion(name)
        sd.gender = gender
        sd.number = num
        sd.text = text
        sd.rev = rev
        texts.append(sd)

    return texts

# Cached old master revisions.
cached_master_files = {}
master_name = None

def get_old_master_text(revision, name):
    """
    Get the old master text of a string at a certain revision.

    @param revision: Revision to pull.
    @type  revision: C{int}

    @param name: String to get.
    @type  name: C{unicode}

    @return: Text and actual revision, if available.
    @rtype:  Tuple (C{unicode}, C{int}) or C{None}
    """
    global master_name, cached_master_files

    assert master_name is not None

    # Find the oldest revision younger or equal to 'revision'
    r = None
    for mf in cached_master_files:
        if mf >= revision and (r is None or r > mf): r = mf

    if r is not None:
        entry = cached_master_files[r].get(name)
        if entry is not None:
            assert len(entry) == 1 # Genders are not supported.
            entry = entry[0]
            if entry.rev is not None and entry.rev <= revision:
                return entry.text, entry.rev

    try:
        data = make_mapping(read_lang(master_name, revision))
    except LanguageReadError, exc:
        print "Warning: Retrieving version information failed: %r" % str(exc.err)
        return None

    cached_master_files[revision] = data
    entry = data.get(name)
    if entry is not None:
        assert len(entry) == 1 # Genders are not supported.
        entry = entry[0]
        return entry.text, entry.rev

    return None


def make_mapping(lines):
    """
    Convert the sequence of lines of a translation to a mapping, so it can
    handle arbitrary ordered string definitions in a translation file.

    @param lines: Loaded translation lines.
    @type  lines: C{list} of L{StringDefintion}

    @return: Mapping of language string to definition sequence (with different gender).
    @rtype:  C{dict} of C{unicode} to C{list} of L{StringDefintion}
    """
    result = {}
    for sd in lines:
        r = result.get(sd.name)
        if r is None:
            result[sd.name] = [sd]
        else:
            r.append(sd)

    return result


def compare_langs(master, translation):
    """
    Compare two languages with each other.

    @param master: Master language definition.
    @type  master: C{list} of L{StringDefintion}

    @param translation: Translation definition.
    @type  translation: C{list} of L{StringDefintion}

    @return: Reports about bad strings (missing, outdated, obsolete).
    @rtype:  Triplet (C{list} of L{StringReport}, C{list} of L{StringReport}, C{list} of L{StringReport})

    @todo: Handle translations from new to old, and shuffle them back in order afterwards.
           This may reduce access to old master language revisions.
    """
    translation = make_mapping(translation) # Convert translation to a dict
    t_names = set(translation.iterkeys()) # names in the translation that have not been processed.

    missing  = [] # Strings missing in the translation.
    outdated = [] # Strings that need to be updated.
    obsolete = [] # Strings not in the master language.
    for m_sd in master:
        assert m_sd.gender is None # Genders for the master language is not supported.
        t_sds = translation.get(m_sd.name)
        if t_sds is None:
            # Missing string
            sr = StringReport(m_sd.name)
            sr.master_text = m_sd.text
            sr.master_line = m_sd.number
            sr.master_rev = m_sd.rev
            missing.append(sr)
            continue

        t_names.remove(m_sd.name) # Matched the string with the master file.

        for t_sd in t_sds:
            if t_sd.rev >= m_sd.rev: continue

            # master rev is newer.
            sr = StringReport(t_sd.get_name())
            sr.trans_text = t_sd.text
            sr.trans_line = t_sd.number
            sr.trans_rev = t_sd.rev
            sr.master_text = m_sd.text
            sr.master_line = m_sd.number
            sr.master_rev = m_sd.rev

            old_textrev = get_old_master_text(t_sd.rev, t_sd.name)
            if old_textrev is not None:
                sr.old_text, sr.old_rev = old_textrev

                if sr.old_text == sr.master_text:
                    # But the old master text is equal to the current master -> false alarm!
                    continue

            outdated.append(sr)


    # Unprocessed translation strings.
    for t_name in t_names:
        t_sds = translation.get(t_name)
        for t_sd in t_sds:
            sr = StringReport(t_sd.get_name())
            sr.trans_text = t_sd.text
            sr.trans_line = t_sd.number
            sr.trans_rev = t_sd.rev
            obsolete.append(sr)

    return missing, outdated, obsolete

