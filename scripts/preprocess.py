#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
from time import time
start = time()

print "[PYTHON] python preprocessing"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join(currentdir, 'src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

import firs

import register_cargos
firs.render_and_save_registered_cargos()

import industries
import register_industries
for industry in industries.registered_industries:
    industry.render_and_save_pnml()

# n.b header items depend on industries being in scope
firs.render_and_save_header_items()

import render_docs

print (time() - start)
