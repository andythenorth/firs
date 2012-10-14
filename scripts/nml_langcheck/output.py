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
import difflib, cgi, os

def make_cell(prefix, val):
    """
    Construct a cell of a table.

    @param prefix: Prefix text to include in front of the value.
    @type  prefix: C{str}

    @param val: Value to add to the cell, if any (output '-' in that case).
    @type  val: C{str} or C{None}

    @return: Text of the cell.
    @rtype:  C{str}
    """
    if val is None: return '<td align="center">-</td>'
    return '<td align="center">' + prefix + str(val) + '</td>'

class HtmlColouredText(object):
    """
    Collect html text where parts have different colours.

    After construction, add text with L{add_white}, L{add_red} and
    L{add_green}. When done, use L{get_text} to get the result.
    """
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
    """
    Construct the diff output.

    @param old: Old version of the string.
    @type  old: C{unicode}

    @param master: String of the current master version.
    @type  master: C{unicode}

    @return: Html-ified diff output of both strings.
    @rtype:  C{tuple} (C{str}, C{str})
    """
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


def pretty_stringreport(report, fp, do_diff):
    """
    Make a pretty HTML report about a L{StringReport}.

    @param report: Report to convert.
    @type  report: L{StringReport}

    @param fp: Output stream.
    @type  fp: C{file}

    @param do_diff: Also output a diff.
    @type  do_diff: C{bool}
    """
    fp.write(('<h3><a name="report_%d">' % report.report_id) + esc_html(report.str_name) + '</a></h3>\n')
    fp.write('<table border="1">\n')
    fp.write('<tr><td>&nbsp;</td><th>Line</th><th>Revision</th><th>Text</th></tr>\n')

    if report.trans_text is not None:
        fp.write('<tr><th align="left">Translation</th>')
        fp.write(make_cell('', report.trans_line) + make_cell('r', report.trans_rev) +
                '<td>' + esc_html(report.trans_text) + '</td></tr>\n')

    if do_diff and report.master_text is not None and report.old_text is not None:
        old, master = make_html_diff(report.old_text, report.master_text)
        fp.write('<tr><th align="left">Current source</th>\n')
        fp.write(make_cell('', report.master_line) + make_cell('r', report.master_rev) +
                '<td>' + master + '</td></tr>\n')
        fp.write('<tr><th align="left">Old source</th>\n')
        fp.write(make_cell('', None) + make_cell('r', report.old_rev) +
                '<td>' + old + '</td></tr>\n')

    else:
        if report.master_text is not None:
            fp.write('<tr><th align="left">Current source</th>\n')
            fp.write(make_cell('', report.master_line) + make_cell('r', report.master_rev) +
                    '<td>' + esc_html(report.master_text) + '</td></tr>\n')

        if report.old_text is not None:
            fp.write('<tr><th align="left">Old source</th>\n')
            fp.write(make_cell('', None) + make_cell('r', report.old_rev) +
                    '<td>' + esc_html(report.old_text) + '</td></tr>\n')

    fp.write('</table>\n')

def print_report(missing, outdated, obsolete, lang_name, fp):
    """
    Output an ASCII version of a language report.

    @param missing: Missing strings.
    @type  missing: C{list} of L{StringReport}

    @param outdated: Outdated strings.
    @type  outdated: C{list} of L{StringReport}

    @param obsolete: Unused strings.
    @type  obsolete: C{list} of L{StringReport}

    @param lang_name: Language name
    @type  lang_name: C{str}

    @param fp: Output stream.
    @type  fp: C{file}
    """
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

    @param missing: Missing strings.
    @type  missing: C{list} of L{StringReport}

    @param outdated: Outdated strings.
    @type  outdated: C{list} of L{StringReport}

    @param obsolete: Unused strings.
    @type  obsolete: C{list} of L{StringReport}

    @param lang_name: Language name
    @type  lang_name: C{str}

    @param fp: Output stream.
    @type  fp: C{file}

    @param do_diff: Also output a diff.
    @type  do_diff: C{bool}
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
            pretty_stringreport(sr, fp, False)

    if len(outdated) > 0:
        fp.write('<h2><a name="outdated">Outdated strings</a></h2>\n')
        for sr in outdated:
            fp.write(('<a href="#report_%d">' % sr.report_id) + esc_html(sr.str_name) + '</a><br>\n')

        for sr in outdated:
            pretty_stringreport(sr, fp, do_diff)

    if len(obsolete) > 0:
        fp.write('<h2><a name="obsolete">Obsolete strings</a></h2>\n')
        for sr in obsolete:
            fp.write(('<a href="#report_%d">' % sr.report_id) + esc_html(sr.str_name) + '</a><br>\n')

        for sr in obsolete:
            pretty_stringreport(sr, fp, False)

    fp.write('</body></html>\n')

def split_path(path):
    """
    Split a path string in its parts.
    """
    parts = []
    while True:
        i = path.find('/')
        j = path.find('\\')
        if i == -1 or (j != -1 and j < i): i = j
        if i == -1: break
        parts.append(path[:i])
        path = path[i+1:]
    parts.append(path)
    return parts

def normalize_path(path):
    parts = split_path(path)
    return "/".join(parts)

def make_relative_path(abs_path, cur_dir):
    i = 0
    while i < len(abs_path) and i < len(cur_dir) and abs_path[i] == cur_dir[i]:
        i = i + 1
    return ['..'] * (len(cur_dir) - i) + abs_path[i:]

class IndexData(object):
    """
    Class for storing information needed for the global index.

    @ivar transl_url: Base url for the translation files, if available.
    @type transl_url: C{str} or C{None}

    @ivar master_count: Number of strings in the master file.
    @type master_count: C{int}

    @ivar index_dir: Absolute directory of the index file, as a sequence of path elements.
    @type index_dir: C{list} of C{str}, or C{None}

    @ivar results: Processing results. List of (language, filename,
                   missing-count, outdated-count, obsolete-count) tuples.
    @type results: C{list} of (C{str}, C{str}, C{int}, C{int}, C{int})
    """
    def __init__(self, transl_url, index_path, master_count):
        self.transl_url = transl_url
        self.master_count = master_count
        if index_path is None:
            self.index_dir = None
        else:
            self.index_dir = split_path(os.path.abspath(index_path))[:-1]

        self.results = []

    def add(self, source, lng, dest, miss_count, outd_count, obs_count):
        """
        Add an entry.

        @param source: Source filename.
        @type  source: C{str}

        @param lng: Name of the language.
        @type  lng: C{str}

        @param dest: Filename of the report.
        @type  dest: C{str}

        @param miss_count: Number of missing strings.
        @type  miss_count: C{int}

        @param outd_count: Number of outdated strings.
        @type  outd_count: C{int}

        @param obs_count: Number of obsolete strings.
        @type  obs_count: C{int}
        """
        bad_strings = miss_count + outd_count
        if bad_strings < obs_count: bad_strings = obs_count
        ok_strings = self.master_count - bad_strings
        if ok_strings < 0: ok_strings = 0
        perc = 100.0 * ok_strings / self.master_count

        if self.index_dir is not None:
            dest = split_path(os.path.abspath(dest))
            dest = "/".join(make_relative_path(dest, self.index_dir))

        report = '<a href="%s">report</a>' % esc_html(dest)
        if self.transl_url is None:
            source = ''
        else:
            source = esc_html(self.transl_url + '/' + normalize_path(source))
            source = ' <a href="%s">file</a>' % source

        line = ['<tr>',
                '<td>%s</td>' % esc_html(lng),
                '<td>%s</td>' % (report + source,),
                '<td>%d</td>' % miss_count,
                '<td>%d</td>' % outd_count,
                '<td>%d</td>' % obs_count,
                '<td>%d/%d = %.1f%%</td>' % (ok_strings, self.master_count, perc),
                '</tr>\n']
        self.results.append((120 - perc, lng, "".join(line)))

    def write_html(self, fname):
        """
        Write the index file.

        @param fname: Name of the index file.
        @type  fname: C{str}
        """
        self.results.sort()

        fp = open(fname, 'w')
        fp.write('<html><head>\n')
        fp.write('<title>Language report</title>\n')
        fp.write('</head><body>\n')
        fp.write('<h1>Language report</h1>\n')
        fp.write('<table border="1">\n')
        line = ['<tr>',
                '<th>Language</th>',
                '<th>Links</th>',
                '<th>Missing</th>',
                '<th>Outdated</th>',
                '<th>Obsolete</th>',
                '<th>Percentage</th>',
                '</tr>\n']
        fp.write("".join(line))
        for entry in self.results:
            fp.write(entry[-1])
        fp.write('</table><p>\n')
        fp.write('<i>missing</i>=Untranslated strings, ')
        fp.write('<i>outdated</i>=Translation needs verification and/or updating, ')
        fp.write('<i>obsolete</i>=String should be removed from the translation.\n')
        fp.write('</body></html>\n')
        fp.close()

