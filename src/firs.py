"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

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

from cargos import alcohol
alcohol.cargo.register()

from cargos import bauxite
bauxite.cargo.register()

from cargos import building_materials
building_materials.cargo.register()

from cargos import chemicals
chemicals.cargo.register()

from cargos import beans
beans.cargo.register()

from cargos import clay
clay.cargo.register()

from cargos import coal
coal.cargo.register()

from cargos import coffee
coffee.cargo.register()

from cargos import copper_ore
copper_ore.cargo.register()

from cargos import diamonds
diamonds.cargo.register()

from cargos import engineering_supplies
engineering_supplies.cargo.register()

from cargos import farm_supplies
farm_supplies.cargo.register()

from cargos import fish
fish.cargo.register()

from cargos import food
food.cargo.register()

from cargos import fruits
fruits.cargo.register()

from cargos import goods
goods.cargo.register()

from cargos import grain
grain.cargo.register()

from cargos import iron_ore
iron_ore.cargo.register()

from cargos import livestock
livestock.cargo.register()

from cargos import lumber
lumber.cargo.register()

from cargos import mail
mail.cargo.register()

from cargos import manufacturing_supplies
manufacturing_supplies.cargo.register()

from cargos import metal
metal.cargo.register()

from cargos import milk
milk.cargo.register()

from cargos import nitrates
nitrates.cargo.register()

from cargos import oil
oil.cargo.register()

from cargos import paper
paper.cargo.register()

from cargos import passengers
passengers.cargo.register()

from cargos import petrol
petrol.cargo.register()

from cargos import plant_fibres
plant_fibres.cargo.register()

from cargos import recyclables
recyclables.cargo.register()

from cargos import rubber
rubber.cargo.register()

from cargos import sand
sand.cargo.register()

from cargos import scrap_metal
scrap_metal.cargo.register()

from cargos import stone
stone.cargo.register()

from cargos import sugar
sugar.cargo.register()

from cargos import sugar_beet
sugar_beet.cargo.register()

from cargos import sugarcane
sugarcane.cargo.register()

from cargos import vehicle_parts
vehicle_parts.cargo.register()

from cargos import wood
wood.cargo.register()

from cargos import wool
wool.cargo.register()


# keep these alphabetised for ease of reading
from industries import aluminium_plant
aluminium_plant.industry.register()

from industries import arable_farm
arable_farm.industry.register()

from industries import basic_farm
basic_farm.industry.register()

from industries import bauxite_mine
bauxite_mine.industry.register()

from industries import biorefinery
biorefinery.industry.register()

from industries import brewery
brewery.industry.register()

from industries import brick_works
brick_works.industry.register()

from industries import builders_yard
builders_yard.industry.register()

from industries import bulk_terminal
bulk_terminal.industry.register()

from industries import cement_plant
cement_plant.industry.register()

from industries import chemical_plant
chemical_plant.industry.register()

from industries import coffee_estate
coffee_estate.industry.register()

from industries import copper_mine
copper_mine.industry.register()

from industries import dairy
dairy.industry.register()

from industries import dairy_farm
dairy_farm.industry.register()

from industries import diamond_mine
diamond_mine.industry.register()

from industries import dredging_site
dredging_site.industry.register()

from industries import fertiliser_plant
fertiliser_plant.industry.register()

from industries import fibre_crop_farm
fibre_crop_farm.industry.register()

from industries import food_market
food_market.industry.register()

from industries import food_processor
food_processor.industry.register()

from industries import furniture_factory
furniture_factory.industry.register()

from industries import general_store
general_store.industry.register()

from industries import glass_works
glass_works.industry.register()

from industries import grain_mill
grain_mill.industry.register()

from industries import hardware_store
hardware_store.industry.register()

from industries import hotel
hotel.industry.register()

from industries import iron_works
iron_works.industry.register()

from industries import junk_yard
junk_yard.industry.register()

from industries import lime_kiln
lime_kiln.industry.register()

from industries import lumber_yard
lumber_yard.industry.register()

from industries import machine_shop
machine_shop.industry.register()

from industries import metal_fabrication_plant
metal_fabrication_plant.industry.register()

from industries import metal_workshop
metal_workshop.industry.register()

from industries import mixed_farm
mixed_farm.industry.register()

from industries import nitrate_mine
nitrate_mine.industry.register()

from industries import oil_wells
oil_wells.industry.register()

from industries import orchard_piggery
orchard_piggery.industry.register()

from industries import petrol_pump
petrol_pump.industry.register()

from industries import plastics_plant
plastics_plant.industry.register()

from industries import ranch
ranch.industry.register()

from industries import recycling_depot
recycling_depot.industry.register()

from industries import recycling_plant
recycling_plant.industry.register()

from industries import rubber_plantation
rubber_plantation.industry.register()

from industries import sheep_farm
sheep_farm.industry.register()

from industries import smithy_forge
smithy_forge.industry.register()

from industries import stockyard
stockyard.industry.register()

from industries import sugar_plantation
sugar_plantation.industry.register()

from industries import sugar_refinery
sugar_refinery.industry.register()

from industries import textile_mill
textile_mill.industry.register()

from industries import trading_post
trading_post.industry.register()

from industries import vehicle_factory
vehicle_factory.industry.register()


# industries which will be hard to convert to python templating, mostly still cpp
from industries import clay_pit
clay_pit.industry.register()

from industries import fishing_grounds
fishing_grounds.industry.register()

from industries import fishing_harbour
fishing_harbour.industry.register()

from industries import forest
forest.industry.register()

from industries import fruit_plantation
fruit_plantation.industry.register()

from industries import port
port.industry.register()

from industries import quarry
quarry.industry.register()


# industries reusing default industry graphics (and possibly default layouts)
from industries import coal_mine
coal_mine.industry.register()

from industries import iron_ore_mine
iron_ore_mine.industry.register()

from industries import oil_refinery
oil_refinery.industry.register()

from industries import oil_rig
oil_rig.industry.register()

from industries import paper_mill
paper_mill.industry.register()

from industries import sawmill
sawmill.industry.register()

from industries import steel_mill
steel_mill.industry.register()


