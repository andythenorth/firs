#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

print "[PYTHON] python preprocessing"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('industries')) # add to the module search path

from industries import bauxite_mine
from industries import food_market
from industries import grain_mill
from industries import oil_wells
