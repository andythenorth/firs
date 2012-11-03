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
sys.path.append(os.path.join('cargos')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

from cargos.alcohol import cargo as alcohol
from cargos.bauxite import cargo as bauxite
from cargos.building_materials import cargo as building_materials
from cargos.chemicals import cargo as chemicals
from cargos.clay import cargo as clay
from cargos.coal import cargo as coal
from cargos.engineering_supplies import cargo as engineering_supplies
from cargos.farm_supplies import cargo as farm_supplies
from cargos.fish import cargo as fish
from cargos.food import cargo as food
from cargos.fruits import cargo as fruits
from cargos.goods import cargo as goods
from cargos.grain import cargo as grain
from cargos.gravel import cargo as gravel
from cargos.iron_ore import cargo as iron_ore
from cargos.livestock import cargo as livestock
from cargos.lumber import cargo as lumber
from cargos.mail import cargo as mail
from cargos.manufacturing_supplies import cargo as manufacturing_supplies
from cargos.milk import cargo as milk
from cargos.oil import cargo as oil
from cargos.passengers import cargo as passengers
from cargos.petrol import cargo as petrol
from cargos.plant_fibres import cargo as plant_fibres
from cargos.recyclables import cargo as recyclables
from cargos.sand import cargo as sand
from cargos.scrap_metal import cargo as scrap_metal
from cargos.steel import cargo as steel
from cargos.sugar_beet import cargo as sugar_beet
from cargos.sugarcane import cargo as sugarcane
from cargos.wood import cargo as wood
from cargos.wool import cargo as wool

cargos = [alcohol, bauxite, building_materials, chemicals, clay, coal, engineering_supplies, farm_supplies, fish,
          food, fruits, goods, grain, gravel, iron_ore, livestock, lumber, mail, manufacturing_supplies, milk,
          oil, passengers, petrol, plant_fibres, recyclables, sand, scrap_metal, steel, sugar_beet, sugarcane, wood, wool]

cargo_output_pnml = []
cargotable = [] # 'cargotable' is a single word in nml
# there is some insanity with cargo.cargo, it's ducktape coding, overlook it.
for cargo in cargos:
    cargo_output_pnml.append(cargo.render_pnml())
    cargotable.append(cargo.cargo_label.replace('"',''))

# save the results of cargo templating
pnml = codecs.open(os.path.join(currentdir,'sprites','nml','generated_pnml', 'cargo_props.pnml'), 'w','utf8')
pnml.write('cargotable{' + ','.join(cargotable) + '}')
pnml.write(''.join(cargo_output_pnml))
pnml.close()

# industries currently take care of rendering themselves to pnml (this comment may age badly)
from industries import biorefinery
from industries import brewery
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
from industries import aluminium_plant
from industries import arable_farm
from industries import brick_works
from industries import builders_yard
from industries import cement_plant
from industries import clay_pit
from industries import dairy
from industries import dairy_farm
from industries import fertiliser_plant
from industries import fishing_grounds
from industries import fishing_harbour
from industries import forest
from industries import fruit_plantation
from industries import furniture_factory
from industries import iron_works
from industries import junk_yard
from industries import lime_kiln
from industries import machine_shop
from industries import metal_fabrication_plant
from industries import metal_workshop
from industries import mixed_farm
from industries import quarry

# industries reusing default industry graphics (and possibly default layouts)
from industries import coal_mine
from industries import iron_ore_mine
from industries import oil_refinery
from industries import oil_rig
from industries import paper_mill
from industries import sawmill
from industries import steel_mill
