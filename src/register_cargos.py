#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
print "[PYTHON] registering cargos"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join(currentdir, 'src')) # add to the module search path

import firs

import cargos
from cargos import alcohol
from cargos import bauxite
from cargos import building_materials
from cargos import chemicals
from cargos import clay
from cargos import coal
from cargos import engineering_supplies
from cargos import farm_supplies
from cargos import fish
from cargos import food
from cargos import fruits
from cargos import goods
from cargos import grain
from cargos import gravel
from cargos import iron_ore
from cargos import livestock
from cargos import lumber
from cargos import mail
from cargos import manufacturing_supplies
from cargos import milk
from cargos import oil
from cargos import passengers
from cargos import petrol
from cargos import plant_fibres
from cargos import recyclables
from cargos import sand
from cargos import scrap_metal
from cargos import steel
from cargos import sugar_beet
from cargos import sugarcane
from cargos import wood
from cargos import wool
