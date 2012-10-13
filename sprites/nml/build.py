#!/usr/bin/env python

print "[PYTHON] python preprocessing"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('industries')) # add to the module search path

from industries import grain_mill
