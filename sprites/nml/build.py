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

from industries import biorefinery
from industries import bauxite_mine
from industries import dredging_site
from industries import food_market
from industries import glass_works
from industries import grain_mill
from industries import hotel
from industries import lumber_yard
from industries import oil_wells
from industries import petrol_pump
from industries import plastics_plant
from industries import recycling_depot
from industries import recycling_plant
from industries import sheep_farm
from industries import smithy_forge
from industries import stockyard
from industries import sugar_refinery
from industries import textile_mill
from industries import hardware_store

# industries with only partial conversion to python templating, mostly still cpp
from industries import coal_mine
from industries import fishing_grounds
from industries import iron_ore_mine
from industries import oil_refinery
from industries import oil_rig
from industries import paper_mill
from industries import sawmill
from industries import steel_mill
