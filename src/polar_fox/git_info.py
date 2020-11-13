"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

#!/usr/bin/env python3

import subprocess

def exe_cmd(cmd):
    try:
        output = subprocess.run(cmd, env=None, check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                    universal_newlines=True).stdout
        lines = output.splitlines()
        return lines
    except:
        return ['undefined']

def get_revision():
    # revision is simply the count of revs in the current branch
    # this won't be perfect in all cases, but there's no possible way to produce a perfect single rev with git
    # so this is good enough
    return exe_cmd(['git', 'rev-list', '--count', 'HEAD'])[0]

def get_version():
    # for the version we just use git describe, which gives us a recent tag or so
    return exe_cmd(['git', 'describe'])[0]

def get_tag_exact_match():
    # are we on a specific tag? (returns tag if true, otherwise errors)
    return exe_cmd(['git', 'describe', '--tags', '--exact-match'])[0]

def run():
    # for the default case we just print the results, this is used by e.g. Makefiles
    # for python cases, use the get_foo methods directly
    print(get_revision(), get_version(), get_tag_exact_match())

if __name__ == '__main__':
    run()
