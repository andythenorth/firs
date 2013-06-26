def get_repo_vars(sys):
    # get args passed by makefile
    if len(sys.argv) > 1:
        repo_vars = {'repo_title' : sys.argv[1], 'repo_version' : sys.argv[2], 'test_industry': sys.argv[3]}
    else: # provide some defaults so templates don't explode when testing python script without command line args
        repo_vars = {'repo_title' : 'FIRS - compiled without makefile', 'repo_version' : 0}
    return repo_vars


def unescape_chameleon_output(escaped_nml):
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = '>'.join(escaped_nml.split('&gt;'))
    escaped_nml = '<'.join(escaped_nml.split('&lt;'))
    escaped_nml = '&'.join(escaped_nml.split('&amp;'))
    return escaped_nml


def parse_base_lang():
    print "[PARSE BASE LANG & EXTRA STRINGS] utils.py"

    import os.path
    currentdir = os.curdir

    import codecs # used for writing files - more unicode friendly than standard open() module

    def split_nml_string_lines(text):
        # this is fragile, playing one line python is silly :)
        return dict((line.split(':',1)[0].strip(), line.split(':',1)[1].strip()) for line in text if ':' in line)

    base_lang_file = codecs.open(os.path.join('lang', 'english.lng'), 'r','utf8')
    strings = split_nml_string_lines(base_lang_file.readlines())

    extra_strings_file = codecs.open(os.path.join('docs_src', 'extra_strings.lng'), 'r','utf8')
    extra_strings = split_nml_string_lines(extra_strings_file.readlines())
    for i in extra_strings:
        strings[i] = extra_strings[i]

    return strings


def unwrap_nml_string_declaration(nml_string=None):
    # some properties are declared in python as 'string(STR_HAM_EGGS)'
    # this is done because it saves hassle with nml (distinguishes from default OTTD strings)
    # doesn't work for direct lookups of string identifier in lang file though, so remove the string() packaging

    if nml_string is not None and 'string(' in nml_string:
        unwrapped_string = nml_string.split('string(')[1][:-1] # split and then slice off the closing bracket
        return unwrapped_string
    else:
        return nml_string

