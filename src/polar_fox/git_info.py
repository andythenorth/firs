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

def run():
    # revision is simply the count of revs in the current branch
    # this won't be perfect in all cases, but there's no possible way to produce a perfect single rev with git
    # so this is good enough
    revision = exe_cmd(['git', 'rev-list', '--count', 'HEAD'])
    # for the version we just use git describe, which gives us a recent tag or so
    version = exe_cmd(['git', 'describe'])

    # are we on a specific tag? (returns tag if true, otherwise errors)
    tag_exact_match = exe_cmd(['git', 'describe', '--tags', '--exact-match'])

    print(revision[0], version[0], tag_exact_match[0])

if __name__ == '__main__':
    run()
