"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

#!/usr/bin/env python3

import subprocess


def exe_cmd(cmd):
    try:
        output = subprocess.run(
            cmd,
            env=None,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            universal_newlines=True,
        ).stdout
        lines = output.splitlines()
        return lines
    except:
        return ["undefined"]


def get_revision():
    # revision is simply the count of revs in the current branch
    # this won't be perfect in all cases, but there's no possible way to produce a perfect single rev with git
    # so this is good enough
    return exe_cmd(["git", "rev-list", "--count", "HEAD"])[0]


def get_version():
    # for the version we just use git describe, which gives us a recent tag or so
    return exe_cmd(["git", "describe"])[0]


def get_tag_exact_match():
    # are we on a specific tag? (returns tag if true, otherwise errors, resulting in "undefined")
    # this could print a more explicit result if "undefined"?  e.g. "no-tag" or so?  Nah might collide with actual tags.
    return exe_cmd(["git", "describe", "--tags", "--exact-match"])[0]


def get_monorepo_tag_parts(repr_type=None):
    # some projects use monorepos to release multiple artefacts
    # each released artefact has its own tag subpath, e.g.
    # horse/1.2.3
    # ibex/3.4.5
    # git will create these tags as actual filesystem subpaths in .git/refs/tags/
    if get_tag_exact_match() != "undefined":
        tag = get_tag_exact_match()
    elif get_version() != "undefined":
        tag = get_version()
    else:
        raise BaseException("Nothing we can use as a tag or tag proxy here: " + get_version())

    parts = tag.split("/")
    if len(parts) == 1:
        # it's not a monorepo tag
        parts.append('not-a-monorepo')
        parts.reverse()
        # it's a monorepo tag in the expected format
    elif len(parts) != 2:
        raise BaseException("Tag or tag proxy has multiple / chars, this isn't supported. " + get_version())
    if repr_type == "shell":
        # for use in makefile
        # not actual shell formatting, just joined on spaces
        # if this turns out to be insufficient, try a shell arg formatter or something
        return ' '.join(parts)
    else:
        return parts

def run():
    # for the default case we just print the results, this is used by e.g. Makefiles
    # for python cases, use the get_foo methods directly
    # note that we print the leading and trailing parts of the tag in the monorepo case (baked-in assumption that only 2 parts exist)
    print(get_revision(), get_version(), get_tag_exact_match(), get_monorepo_tag_parts(repr_type="shell"))


if __name__ == "__main__":
    run()
