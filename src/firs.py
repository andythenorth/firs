"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

import codecs # used for writing files - more unicode friendly than standard open() module

import os
currentdir = os.curdir
# add to the module search path
src_path = os.path.join(currentdir, 'src')

import global_constants

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

from cargos import registered_cargos

from cargos import alcohol
from cargos import bauxite
from cargos import building_materials
from cargos import chemicals
from cargos import clay
from cargos import coal
from cargos import coffee
from cargos import copper_ore
from cargos import diamonds
from cargos import engineering_supplies
from cargos import farm_supplies
from cargos import fish
from cargos import food
from cargos import fruits
from cargos import goods
from cargos import grain
from cargos import iron_ore
from cargos import livestock
from cargos import lumber
from cargos import mail
from cargos import manufacturing_supplies
from cargos import metal
from cargos import milk
from cargos import oil
from cargos import paper
from cargos import passengers
from cargos import petrol
from cargos import plant_fibres
from cargos import recyclables
from cargos import rubber
from cargos import sand
from cargos import scrap_metal
from cargos import stone
from cargos import sugar
from cargos import sugar_beet
from cargos import sugarcane
from cargos import wood
from cargos import wool


import industry
from industries import registered_industries

from industries import aluminium_plant
from industries import arable_farm
from industries import basic_farm
from industries import bauxite_mine
from industries import biorefinery
from industries import brewery
from industries import brick_works
from industries import builders_yard
from industries import bulk_terminal
from industries import cement_plant
from industries import coffee_estate
from industries import copper_mine
from industries import dairy
from industries import dairy_farm
from industries import diamond_mine
from industries import dredging_site
from industries import fertiliser_plant
from industries import fibre_crop_farm
from industries import food_market
from industries import furniture_factory
from industries import general_store
from industries import glass_works
from industries import grain_mill
from industries import hardware_store
from industries import hotel
from industries import iron_works
from industries import junk_yard
from industries import lime_kiln
from industries import lumber_yard
from industries import machine_shop
from industries import metal_fabrication_plant
from industries import metal_workshop
from industries import mixed_farm
from industries import oil_wells
from industries import orchard_piggery
from industries import petrol_pump
from industries import plastics_plant
from industries import ranch
from industries import recycling_depot
from industries import recycling_plant
from industries import rubber_plantation
from industries import sheep_farm
from industries import smithy_forge
from industries import stockyard
from industries import sugar_plantation
from industries import sugar_refinery
from industries import textile_mill
from industries import trading_post

# industries which will be hard to convert to python templating, mostly still cpp
from industries import clay_pit
from industries import fishing_grounds
from industries import fishing_harbour
from industries import forest
from industries import fruit_plantation
from industries import port
from industries import quarry

# industries reusing default industry graphics (and possibly default layouts)
from industries import coal_mine
from industries import iron_ore_mine
from industries import oil_refinery
from industries import oil_rig
from industries import paper_mill
from industries import sawmill
from industries import steel_mill

