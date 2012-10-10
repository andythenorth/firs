#!/usr/bin/env python
"""
License:
    'cl' is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    'cl' is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

Check language files of NML project, and report missing, outdated, and obsolete strings.
Output can be in text, or in pretty html.

Oct 10, 2012 (cl 2.2)
 - Added index generation (--index option)

May 3, 2012 (cl 2.1)
 - Added --ext EXT, --output-dir DIR options, and allow several translation files.

May 1, 2012
 - Release of first version, cl 2.0

"""
import subprocess, os, sys, re, codecs, cgi, getopt, difflib

_version = '2.2'

class LanguageReadError(Exception):
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

def make_cell(prefix, val):
    if val is None: return '<td align="center">-</td>'
    return '<td align="center">' + prefix + str(val) + '</td>'

class HtmlColouredText(object):
    def __init__(self):
        self.txt = []
        self.col = 'w'

    def add_white(self, t):
        if self.col != 'w':
            self.txt.append('</span>')
            self.col = 'w'
        if t != '': self.txt.append(t)

    def add_red(self, t):
        if self.col != 'r':
            self.txt.append('</span><span style="background-color:#FFAAAA;">')
            self.col = 'r'
        self.txt.append(t)

    def add_green(self, t):
        if self.col != 'g':
            self.txt.append('</span><span style="background-color:#AAFFAA;">')
            self.col = 'g'
        self.txt.append(t)

    def get_text(self):
        self.add_white('')
        return ''.join(self.txt)


def make_html_diff(old, master):
    m = HtmlColouredText()
    o = HtmlColouredText()
    for line in difflib.ndiff(old, master):
        txt = esc_html(line[-1])
        if line[0] == ' ':
            m.add_white(txt)
            o.add_white(txt)
        elif line[0] == '-':
            o.add_red(txt)
        elif line[0] == '+':
            m.add_green(txt)
        else:
            assert 0 # Not expected.

    return o.get_text(), m.get_text()



report_number = 1


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

    def pretty_report(self, fp, do_diff):
        fp.write(('<h3><a name="report_%d">' % self.report_id) + esc_html(self.str_name) + '</a></h3>\n')
        fp.write('<table border="1">\n')
        fp.write('<tr><td>&nbsp;</td><th>Line</th><th>Revision</th><th>Text</th></tr>\n')

        if self.trans_text is not None:
            fp.write('<tr><th align="left">Translation</th>')
            fp.write(make_cell('', self.trans_line) + make_cell('r', self.trans_rev) +
                    '<td>' + esc_html(self.trans_text) + '</td></tr>\n')

        if do_diff and self.master_text is not None and self.old_text is not None:
            old, master = make_html_diff(self.old_text, self.master_text)
            fp.write('<tr><th align="left">Current source</th>\n')
            fp.write(make_cell('', self.master_line) + make_cell('r', self.master_rev) +
                    '<td>' + master + '</td></tr>\n')
            fp.write('<tr><th align="left">Old source</th>\n')
            fp.write(make_cell('', None) + make_cell('r', self.old_rev) +
                    '<td>' + old + '</td></tr>\n')

        else:
            if self.master_text is not None:
                fp.write('<tr><th align="left">Current source</th>\n')
                fp.write(make_cell('', self.master_line) + make_cell('r', self.master_rev) +
                        '<td>' + esc_html(self.master_text) + '</td></tr>\n')

            if self.old_text is not None:
                fp.write('<tr><th align="left">Old source</th>\n')
                fp.write(make_cell('', None) + make_cell('r', self.old_rev) +
                        '<td>' + esc_html(self.old_text) + '</td></tr>\n')

        fp.write('</table>\n')


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

    p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    reader = codecs.getreader('utf-8')(p.stdout)
    for idx, line in enumerate(reader.readlines()):
        if idx == 0 and line[0] == utf8_bom: line = line[1:]
        line = line.rstrip()
        m = re_annot.match(line)
        if not m: print repr(line)
        assert m
        i = m.end()
        if len(line) > i and line[i] == ' ': i = i + 1
        if idx == 0  and len(line) > i and line[i] == utf8_bom: i = i + 1

        if len(line) == i:
            yield int(m.group(1)), idx + 1, u''
        else:
            yield int(m.group(1)), idx + 1, line[i:]

    p.wait()
    if p.returncode != 0:
        raise LanguageReadError(u'Non-zero exit code while annotating %r' % fname)


def read_lang(fname, revision):
    """
    Read the language file, and returns its strings, and the last changed revision.

    @param fname: Filename to load.
    @type  fname: C{str}

    @param revision: Revision to query.
    @type  revision: C{int} or C{None}

    @return: Sequence of read language strings.
    @rtype:  C{list} of L{StringDefintion}

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
    except LanguageReadError, err:
        print "Failure: %r" % str(err)
        print "Skipping old revision retrieval"
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

def print_report(missing, outdated, obsolete, lang_name, fp):
    txt = 'Report for ' + lang_name
    fp.write(txt + '\n')
    fp.write('=' * len(txt))
    fp.write('\n')
    fp.write('Number of missing  strings: %d\n' % len(missing))
    fp.write('Number of outdated strings: %d\n' % len(outdated))
    fp.write('Number of obsolete strings: %d\n' % len(obsolete))
    fp.write('\n')

    flag = False
    if len(missing) > 0:
        flag = True
        fp.write('Missing strings\n')
        fp.write('---------------\n')
        for sr in missing:
            sr.write(fp)
            fp.write('\n')

    if len(outdated) > 0:
        flag = True
        fp.write('\n')
        fp.write('Outdated strings\n')
        fp.write('----------------\n')
        for sr in outdated:
            sr.write(fp)
            fp.write('\n')

    if len(obsolete) > 0:
        flag = True
        fp.write('\n')
        fp.write('Obsolete strings\n')
        fp.write('----------------\n')
        for sr in obsolete:
            sr.write(fp)
            fp.write('\n')

    if not flag:
        fp.write('Completely up to date!\n')

def esc_html(ucode):
    ucode = cgi.escape(ucode)
    return ucode.encode('ascii', 'xmlcharrefreplace')

def pretty_report(missing, outdated, obsolete, lang_name, fp, do_diff):
    """
    Make a report in HTML
    """
    txt = esc_html(lang_name)
    fp.write('<html><head>\n')
    fp.write('<title>Report for ' + txt + '</title>\n')
    fp.write('</head><body>\n')
    fp.write('<h1>Report for <i>' + txt + '</i></h1>\n')
    fp.write('<table>\n')
    mtext = 'missing strings'
    if len(missing) > 0: mtext = '<a href="#missing">' + mtext + '</a>'
    fp.write('<tr><td>Number of ' + mtext + '</td><td>%d</td></tr>\n' % len(missing))
    otext = 'outdated strings'
    if len(outdated) > 0: otext = '<a href="#outdated">' + otext + '</a>'
    fp.write('<tr><td>Number of ' + otext + '</td><td>%d</td></tr>\n' % len(outdated))
    otext = 'obsolete strings'
    if len(obsolete) > 0: otext = '<a href="#obsolete">' + otext + '</a>'
    fp.write('<tr><td>Number of ' + otext + '</td><td>%d</td></tr>\n' % len(obsolete))
    fp.write('</table>\n')

    if len(missing) > 0:
        fp.write('<h2><a name="missing">Missing strings</a></h2>\n')
        for sr in missing:
            fp.write(('<a href="#report_%d">' % sr.report_id) + esc_html(sr.str_name) + '</a><br>\n')

        for sr in missing:
            sr.pretty_report(fp, False)

    if len(outdated) > 0:
        fp.write('<h2><a name="outdated">Outdated strings</a></h2>\n')
        for sr in outdated:
            fp.write(('<a href="#report_%d">' % sr.report_id) + esc_html(sr.str_name) + '</a><br>\n')

        for sr in outdated:
            sr.pretty_report(fp, do_diff)

    if len(obsolete) > 0:
        fp.write('<h2><a name="obsolete">Obsolete strings</a></h2>\n')
        for sr in obsolete:
            fp.write(('<a href="#report_%d">' % sr.report_id) + esc_html(sr.str_name) + '</a><br>\n')

        for sr in obsolete:
            sr.pretty_report(fp, False)

    fp.write('</body></html>\n')

class IndexData(object):
    """
    Class for storing information needed for the global index.

    @ivar results: Processing results. List of (language, filename, missing, outdated, obsolete) tuples.
    @type results: C{list} of (C{str}, C{str}, C{int}, C{int}, C{int})
    """
    def __init__(self):
        self.results = []

    def add(self, lng_name, filename, missing_count, outdated_count, obsolete_count):
        self.results.append((lng_name, filename, missing_count, outdated_count, obsolete_count))

    def write_html(self, fname, master_count):
        if os.sep in fname:
            prefix = os.path.dirname(fname) + os.sep
        else:
            prefix = None

        langs = []
        for lng, lngname, miss, out, obso in self.results:
            if prefix is not None and lngname.startswith(prefix):
                lngname = lngname[len(prefix):]
            t,f = esc_html(lng), esc_html(lngname)
            ok_strings = master_count - miss - out
            if ok_strings < 0: ok_strings = 0
            perc = 100.0 * ok_strings / master_count
            s = '<tr><td><a href="%s">%s</a></td><td>%d</td><td>%d</td><td>%d</td><td>%d/%d = %.1f%%</td></tr>\n' \
                     % (f, t, miss, out, obso, ok_strings, master_count, perc)
            langs.append((120 - perc, lng, s))
        langs.sort()

        fp = open(fname, 'w')
        fp.write('<html><head>\n')
        fp.write('<title>Language report</title>\n')
        fp.write('</head><body>\n')
        fp.write('<h1>Language report</h1>\n')
        fp.write('<table border="1">\n')
        fp.write('<tr><th>Language</th><th>Missing</th><th>Outdated</th><th>Obsolete</th><th>Percentage</th></tr>\n')
        for entry in langs:
            fp.write(entry[-1])
        fp.write('</table><p>\n')
        fp.write('<i>missing</i>=Untranslated strings, ')
        fp.write('<i>outdated</i>=Translation needs verification and/or updating, ')
        fp.write('<i>obsolete</i>=String should be removed from the translation.\n')
        fp.write('</body></html>\n')
        fp.close()


class CmdLine(object):
    """
    Class for storing and accessing cmd-line information.

    @ivar html: Output in html format.
    @type html: C{bool}

    @ivar diff: Also perform 'diff' output between master language revisions.
    @type diff: C{bool}

    @ivar out_dir: Output directory, if specified.
    @type out_dir: C{None} or C{str}

    @ivar ext: Extension to strip.
    @type ext: C{str}

    @ivar master: Name of the master file.
    @type master: C{str}

    @ivar transls: Translation files.
    @type transls: C{list} of C{str}

    @ivar verbose: Verbosity level (higher means more output).
    @type verbose: C{int}

    @ivar index_name: Output filename of the index file (or C{None}).
    @type index_name: C{str} or C{None}
    """
    def __init__(self):
        self.html = False
        self.diff = False
        self.out_dir = None
        self.ext = ".lng"
        self.master = None
        self.transls = []
        self.verbose = 0
        self.index_name = None

    def set_args(self, args):
        if len(args) == 0: return
        self.master = args[0]
        self.transls = [fname for fname in args[1:] if fname != self.master]

    def get_error(self):
        """
        Is the command line configuration OK to proceed?

        @return: Error description if a problem is found.
        @rtype:  C{str} or C{None}
        """
        if self.out_dir is not None and not os.path.isdir(self.out_dir):
            return "Output directory %r is not a directory" % self.out_dir

        if self.master is None:
            return "Missing master language."

        if not os.path.isfile(self.master):
            return "Path %r does not point to a master file." % self.master

        if self.out_dir is None and len(self.transls) > 1:
            return "At most one translation is allowed when not using --output-dir."

        return None # All is fine!

    def get_jobs(self):
        """
        Get the translation jobs to do.

        @return: A sequence of source files to process, and destinations to
                 write to (C{None} for stdout)
        @rtype:  C{list} of (C{str}, C{str} or C{None})
        """
        jobs = []
        for orig in self.transls:
            if self.out_dir is None:
                jobs.append((orig, None))
                continue

            dest = os.path.basename(orig)
            if len(self.ext) > 0 and len(dest) > len(self.ext) and dest.endswith(self.ext):
                dest = dest[:-len(self.ext)]
            if self.html:
                dest = os.path.join(self.out_dir, dest + ".html")
            else:
                dest = os.path.join(self.out_dir, dest + ".log")
            jobs.append((orig, dest))
        return jobs

def usage(fp):
    fp.write('Usage: cl [options] <master-file> <translation-file...>\n')
    fp.write('with options:\n')
    fp.write('    -h, --help        This help\n')
    fp.write('    --html            Output pretty html\n')
    fp.write('    -d, --diff        Make coloured diffing in the source strings (html only)\n')
    fp.write('    --output-dir=DIR  Put results in this directory\n')
    fp.write('    --index=FILE      Write file FILE for the index (only with --output-dir)\n')
    fp.write('    -e EXT, --ext EXT Strip extension EXT from the filename (default .lng)\n')
    fp.write('    --verbose         Be more verbose about progress\n')
    fp.write('\n')
    fp.write('Version ' + _version + '\n')


def process_cmdline():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "e:dh",
                     ["verbose", "ext", "output-dir=", "index=", "diff", "help", "html"])
    except getopt.GetoptError, err:
        print "cl: " + str(err)
        usage(sys.stdout)
        sys.exit(2)

    cmd_line = CmdLine()
    for o, a in opts:
        if o == "--html":
            cmd_line.html = True
        elif o in ("-d", "--diff"):
            cmd_line.diff = True
        elif o in ("-h", "--help"):
            usage(sys.stdout)
            sys.exit(0)
        elif o in ('-e', '--ext'):
            cmd_line.ext = a
        elif o == '--output-dir':
            cmd_line.out_dir = a
        elif o == '--verbose':
            cmd_line.verbose = cmd_line.verbose + 1
        elif o == '--index':
            cmd_line.index_name = a
        else:
            raise RuntimeError("Unknown exception encountered")

    if not cmd_line.html: cmd_line.do_diff = False
    if cmd_line.out_dir is None: cmd_line.index_name = None

    cmd_line.set_args(args)

    err = cmd_line.get_error()
    if err is not None:
        print "cl: " + err
        print
        usage(sys.stdout)
        sys.exit(1)

    return cmd_line

def main():
    global master_name

    cmd_line = process_cmdline()
    master_name = cmd_line.master
    index_data = IndexData()

    master_data = read_lang(master_name, None)
    for src, dest in cmd_line.get_jobs():
        if cmd_line.verbose > 0:
            print "%r -> %r" % (src, dest)

        translation = read_lang(src, None)

        missing, outdated, obsolete = compare_langs(master_data, translation)
        if dest is None:
            fp = sys.stdout
        else:
            fp = open(dest, 'wt')
            index_data.add(src, dest, len(missing), len(outdated), len(obsolete))

        if cmd_line.html:
            pretty_report(missing, outdated, obsolete, src, fp, cmd_line.diff)
        else:
            print_report(missing, outdated, obsolete, src, fp)

        if dest is not None: fp.close()

    if cmd_line.index_name is not None:
        index_data.write_html(cmd_line.index_name, len(master_data))

if __name__ == "__main__":
    main()

