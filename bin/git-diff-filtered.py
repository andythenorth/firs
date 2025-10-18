#!/usr/bin/env python3

import subprocess

EXCLUDES = [
    "src/cargos",
    "src/docs",
    "src/economies",
    "src/global_constants.py",
    "src/industries",
    "src/graphics",
    "src/lang",
    "src/grf/lang",
]

cmd = ["git", "diff", "main..mild-mild-west", "--", "."]

for path in EXCLUDES:
    cmd.append(f":(exclude){path}")

subprocess.run(cmd)
