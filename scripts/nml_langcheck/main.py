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

Check language files of NML project, and report missing, outdated, and obsolete strings.
Output can be in text, or in pretty html.

Oct 12, 2012 (nml_langcheck 2.3)
 - Application has a new name.
 - Moved to http://dev.openttdcoop.org/projects/make-nml-common/ .
 - Output directory is automagically created when it does not exist yet.
 - Added --cfg=FILE option to load settings from an [options] section in that file.
 - Added a --transl-url option to allow references to the language files.

Oct 10, 2012 (cl 2.2)
 - Added index generation (--index option)

May 3, 2012 (cl 2.1)
 - Added --ext EXT, --output-dir DIR options, and allow several translation files.

May 1, 2012
 - Release of first version, cl 2.0

"""
import os, sys, getopt, ConfigParser
from nml_langcheck import output, languages

_version = '2.3'


class CmdLine(object):
    """
    Class for storing and accessing cmd-line information.

    @cvar short_opts: Short option names.
    @type short_opts: C{str}

    @cvar long_opts: Long option names.
    @type long_opts: C{str}

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

    @ivar transl_url: Base url for getting the current language file, if set.
    @type transl_url: C{str} or C{None}

    @ivar verbose: Verbosity level (higher means more output).
    @type verbose: C{int}

    @ivar index_name: Output filename of the index file (or C{None}).
    @type index_name: C{str} or C{None}
    """
    short_opts = "e:dh"
    long_opts = ["verbose", "ext", "output-dir=", "index=", "diff", "help",
                 "cfg=", "html", "transl-url="]

    def __init__(self):
        self.html = False
        self.diff = False
        self.out_dir = None
        self.ext = ".lng"
        self.master = None
        self.transls = []
        self.transl_url = None
        self.verbose = 0
        self.index_name = None

    def process_option(self, opt, arg, allow_help, allow_cfg):
        """
        Process an option.

        @param opt: Name of the option.
        @type  opt: C{str}

        @param arg: Text of the option value, if available.
        @type  arg: C{str} or C{None}

        @param allow_help: Allow the -h/--help option.
        @type  allow_help: C{bool}

        @param allow_cfg: Allow the --cfg option.
        @type  allow_cfg: C{bool}

        @return: Option was successfully processed.
        @rtype:  C{bool}
        """
        if opt == "--html":
            self.html = True
            return True

        if opt in ("-d", "--diff"):
            self.diff = True
            return True

        if opt in ("-h", "--help"):
            if allow_help:
                usage(sys.stdout)
                sys.exit(0)
            else:
                print "Warning: Skipped the --help option."
            return True

        if opt in ('-e', '--ext'):
            self.ext = arg
            return True

        if opt == '--output-dir':
            self.out_dir = arg
            return True

        if opt == '--verbose':
            self.verbose = self.verbose + 1
            return True

        if opt == '--index':
            self.index_name = arg
            return True

        if opt == '--transl-url':
            self.transl_url = arg
            return True

        if opt == '--cfg':
            if allow_cfg:
                self.load_cfg(arg)
            else:
                print "Warning: Skipped the --cfg option."
            return True

        return False

    def load_cfg(self, fname):
        """
        Load options from an INI file, in the [options] section.

        @param fname: Name of the INI file.
        @type  fname: C{str}
        """
        cfg_parser = ConfigParser.SafeConfigParser()
        cfg_parser.read([fname])
        if not cfg_parser.has_section('options'): return

        for opt, arg in cfg_parser.items('options'):
            if self.process_option('--' + opt, arg, False, False): continue

            msg = "Unknown option '--%s' encountered in option file '%s'" \
                % (opt, fname)

            print "Warning: " + msg


    def set_args(self, args):
        """
        Set the command-line arguments of this run.

        @param args: Arguments left after option processing.
        @type  args: C{list} of C{str}
        """
        if len(args) == 0: return
        self.master = args[0]
        self.transls = [fname for fname in args[1:] if fname != self.master]

    def get_error(self):
        """
        Is the command line configuration OK to proceed?

        @return: Error description if a problem is found.
        @rtype:  C{str} or C{None}
        """
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

        @return: A sequence of source file to process, name of the language,
                 and destination to write to (C{None} for stdout).
        @rtype:  C{list} of (C{str}, C{str}, C{str} or C{None})
        """
        jobs = []
        for orig in self.transls:
            dest = os.path.basename(orig)
            if self.out_dir is None:
                jobs.append((orig, dest, None))
                continue

            if len(self.ext) > 0 and len(dest) > len(self.ext) and dest.endswith(self.ext):
                dest = dest[:-len(self.ext)]
            base = dest

            if self.html:
                dest = os.path.join(self.out_dir, dest + ".html")
            else:
                dest = os.path.join(self.out_dir, dest + ".log")

            jobs.append((orig, base, dest))
        return jobs


usage_text = """\
Usage: nml_langcheck [options] <master-file> <translation-file...>
with options:
    --cfg=FILE        Load options from the ini FILE ([options] section),
                      overwrites previously set options.
    -d, --diff        Make coloured diffing in the source strings (html only).
    -e EXT, --ext EXT Strip extension EXT from the filename (default .lng).
    -h, --help        This help.
    --html            Output pretty html.
    --index=FILE      Write file FILE for the index (only with --output-dir).
    --output-dir=DIR  Put results in this directory.
    --transl-url=URL  Base url for retrieving a language file, the path of
                      <translation-file> gets appended.
    --verbose         Be more verbose about progress.

Version $VERSION
"""

def usage(fp):
    fp.write(usage_text.replace('$VERSION', _version))

def process_cmdline():
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   CmdLine.short_opts, CmdLine.long_opts)
    except getopt.GetoptError, err:
        print "nml_langcheck: " + str(err)
        usage(sys.stdout)
        sys.exit(2)

    cmd_line = CmdLine()
    for opt, arg in opts:
        if cmd_line.process_option(opt, arg, True, True): continue

        raise RuntimeError("Unknown option encountered")

    if not cmd_line.html: cmd_line.do_diff = False
    if cmd_line.out_dir is None: cmd_line.index_name = None

    cmd_line.set_args(args)

    err = cmd_line.get_error()
    if err is not None:
        print "nml_langcheck: " + err
        print
        usage(sys.stdout)
        sys.exit(1)

    return cmd_line


def check_outdir(out_dir_path):
    """
    Check whether the output dir exists, and create it if needed.

    @param out_dir_path: Path to check/create.
    @type  out_dir_path: C{str} or C{None} if no directory needed.
    """
    if out_dir_path is None or os.path.isdir(out_dir_path): return

    path = os.path.abspath(out_dir_path)
    os.makedirs(path)


def get_language(fname):
    """
    Retrieve the current version of a language.

    @param fname: Filename of the language.
    @type  fname: C{str}

    @return: Sequence of loaded language strings or nothing.
    @rtype:  C{list} of L{StringDefintion}, or C{None}
    """
    try:
        return languages.read_lang(fname, None)
    except languages.LanguageReadError, exc:
        print "Language file \"%s\" cannot be found: %r" % (fname, str(exc.err))
        return None


def main():
    cmd_line = process_cmdline()
    languages.master_name = cmd_line.master

    master_data = get_language(cmd_line.master)
    if master_data is None:
        print "Quitting!"
        sys.exit(1)

    index_data = output.IndexData(cmd_line.transl_url, cmd_line.index_name, len(master_data))
    checked_outdir = False # Did we verify that cmd_line.out_dir exists?

    for src, lang_name, dest in cmd_line.get_jobs():
        if cmd_line.verbose > 0:
            print "%r -> %r" % (src, dest)

        translation = get_language(src)
        if translation is None:
            print "Quitting!"
            sys.exit(1)

        missing, outdated, obsolete = languages.compare_langs(master_data, translation)
        if dest is None:
            fp = sys.stdout
        else:
            if not checked_outdir:
                check_outdir(cmd_line.out_dir)
                checked_outdir = True

            fp = open(dest, 'wt')
            index_data.add(src, lang_name, dest, len(missing), len(outdated), len(obsolete))

        if cmd_line.html:
            output.pretty_report(missing, outdated, obsolete, src, fp, cmd_line.diff)
        else:
            output.print_report(missing, outdated, obsolete, src, fp)

        if dest is not None: fp.close()

    if cmd_line.index_name is not None:
        if not checked_outdir:
            check_outdir(cmd_line.out_dir)
            checked_outdir = True

        index_data.write_html(cmd_line.index_name)

if __name__ == "__main__":
    main()

