"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import Industry, Tile, Sprite, Spriteset, SpriteLayout, IndustryLayout
import global_constants

"""
Notes to self whilst figuring out python-firs (notes will probably rot here forever).
By convention, ids for use in nml have industry name prefix, local python object ids don't bother with industry name prefix.
Some method properties expect object references, and the templating then uses properties from that object.
Some method properties need a string - the templating is then typically directly writing out an nml identifier.
When a string is expected are basically two choices: provide a string directly, or make an object reference and get an id from that object.
"""

industry = Industry(id='bulk_terminal',
                    accept_cargo_types=['FOOD', 'FRUT', 'BEER'],
                    input_multiplier_1='[0, 0]',
                    input_multiplier_3='[0, 0]',
                    input_multiplier_2='[0, 0]',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='2',
                    prob_random='6',
                    prod_multiplier='[9, 9]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='175',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    min_cargo_distr='2',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER)',
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_BULK_TERMINAL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_HARBOUR))',
                    fund_cost_multiplier='152',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    override_default_construction_states=True,
                    supply_requirements=global_constants.supply_requirements['import_export'])

industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].accept_cargo_types = ['OIL_', 'CORE', 'SUGR']
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['BDMT', 'GRAI']

industry.add_tile(id='bulk_terminal_tile')

#empty tile
#covered store
#tanks
#silos
#cone silo
#warehouse LHS
#warehouse RHS
#bulk staithe LHS
#bulk staithe RHS
#large crane
#boat 1
#boat 2

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_ground',
    type = 'empty'
)
spriteset_concrete = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_1',
    sprites = [(10, 10, 64, 39, -31, -8)],
    always_draw = 1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_2',
    sprites = [(10, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_3',
    sprites = [(80, 60, 64, 39, -31, -7)],
    zextent = 7,
    always_draw = 1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_4',
    sprites = [(150, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_5',
    sprites = [(220, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_6',
    sprites = [(290, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_7',
    sprites = [(360, 60, 64, 39, -31, -7)],
    zextent = 7
)
spriteset_covered_store = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_8',
    sprites = [(150, 10, 64, 39, -31, 0)],
    yoffset = 4,
    zoffset = 27,
    yextent = 12,

)
#bulk_terminal_spriteset_9 unused
spriteset_tanks = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_10',
    sprites = [(80, 10, 64, 39, -31, 0)],
    zoffset = 18
)
spriteset_silos = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_11',
    sprites = [(510, 10, 64, 39, -35, -15)],
)
spriteset_cone_silo = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_12',
    sprites = [(580, 10, 64, 39, -31, -14)],
)
spriteset_warehouse_lhs = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_13',
    sprites = [(650, 10, 64, 39, -31, -8)],
)
spriteset_warehouse_rhs = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_14',
    sprites = [(720, 10, 64, 39, -27, -12)],
)
spriteset_staithe_lhs = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_15',
    sprites = [(440, 110, 64, 39, -15, -11)],
)
spriteset_staithe_rhs = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_16',
    sprites = [(510, 110, 64, 39, -45, -15)],
)
spriteset_large_crane = industry.add_spriteset(
    id = 'bulk_terminal_spriteset_17',
    sprites = [(580, 110, 64, 39, -31, 0)],
    zoffset = 18,
)

industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_1',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_4',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_5',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_6',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_7',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_8',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_9',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_large_crane]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_10',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_11',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_12',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_13',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_14',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_15',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_slope_nw_se, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_16',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_ne_sw, spriteset_jetty_se_nw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_17',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_18',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_se_nw, spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_19',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_slope_sw_ne, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_20',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_21',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_silos]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_22',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_cone_silo]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_23',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_warehouse_lhs]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_24',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_warehouse_rhs]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_25',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_warehouse_rhs]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_26',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_staithe_lhs]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_27',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_staithe_rhs]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_28',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_covered_store]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_29',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_tanks]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_30',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = [spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete]
)
industry.add_spritelayout(
    id = 'bulk_terminal_spritelayout_null',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_empty,
    building_sprites = []
)

industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_1',
    layout = [(0, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_27'),
              (0, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (1, 0, '255', 'bulk_terminal_spritelayout_null'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_29'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (1, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_27'),
              (3, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (4, 0, '255', 'bulk_terminal_spritelayout_null'),
              (4, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (4, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_29'),
              (4, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (4, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (5, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (5, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (5, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_2',
    layout = [(0, 0, '255', 'bulk_terminal_spritelayout_null'),
              (0, 1, '255', 'bulk_terminal_spritelayout_null'),
              (0, 2, '255', 'bulk_terminal_spritelayout_null'),
              (1, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_23'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_23'),
              (1, 255, '255', 'bulk_terminal_spritelayout_null'),
              (2, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_30'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_12'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_21'),
              (2, 255, '255', 'bulk_terminal_spritelayout_null'),
              (3, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_30'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_12'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_21'),
              (3, 255, '255', 'bulk_terminal_spritelayout_null'),
              (4, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_30'),
              (4, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_12'),
              (4, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_21'),
              (4, 255, '255', 'bulk_terminal_spritelayout_null'),
              (5, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_30'),
              (5, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_12'),
              (5, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_21'),
              (5, 255, '255', 'bulk_terminal_spritelayout_null'),
              (6, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (6, 1, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_3',
    layout = [(0, 1, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (0, 2, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (0, 3, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (1, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_2'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_26'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (2, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_22'),
              (2, 5, '255', 'bulk_terminal_spritelayout_null'),
              (3, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_2'),
              (3, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_22'),
              (4, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_26'),
              (4, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (4, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (4, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_22'),
              (4, 5, '255', 'bulk_terminal_spritelayout_null'),
              (5, 2, '255', 'bulk_terminal_spritelayout_null'),
              (5, 3, '255', 'bulk_terminal_spritelayout_null'),
              (5, 4, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_4',
    layout = [(0, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (0, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (0, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_1'),
              (0, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_29'),
              (0, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_13'),
              (0, 5, '255', 'bulk_terminal_spritelayout_null'),
              (1, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_25'),
              (1, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_25'),
              (1, 5, '255', 'bulk_terminal_spritelayout_null'),
              (2, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_2'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_11'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_1'),
              (2, 3, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_29'),
              (2, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_13'),
              (2, 5, '255', 'bulk_terminal_spritelayout_null'),
              (3, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (3, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_28'),
              (3, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_25'),
              (3, 4, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_25'),
              (3, 5, '255', 'bulk_terminal_spritelayout_null'),
              (4, 3, '255', 'bulk_terminal_spritelayout_null'),
              (4, 4, '255', 'bulk_terminal_spritelayout_null'),
              (4, 5, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id = 'bulk_terminal_industry_layout_5',
    layout = [(0, 0, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 1, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 4, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 5, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (0, 6, 'bulk_terminal_tile_2', 'bulk_terminal_slope_switch_1'),
              (1, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_3'),
              (1, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_29'),
              (1, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_3'),
              (1, 5, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_13'),
              (1, 6, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_13'),
              (1, 7, '255', 'bulk_terminal_spritelayout_null'),
              (2, 255, '255', 'bulk_terminal_spritelayout_null'),
              (2, 0, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 1, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 2, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 5, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 6, 'bulk_terminal_tile_1', 'bulk_terminal_spritelayout_24'),
              (2, 7, '255', 'bulk_terminal_spritelayout_null'),
              (3, 255, '255', 'bulk_terminal_spritelayout_null'),
              (3, 0, '255', 'bulk_terminal_spritelayout_null'),
              (3, 1, '255', 'bulk_terminal_spritelayout_null'),
              (3, 2, '255', 'bulk_terminal_spritelayout_null'),
              (3, 3, '255', 'bulk_terminal_spritelayout_null'),
              (3, 4, '255', 'bulk_terminal_spritelayout_null'),
              (3, 5, '255', 'bulk_terminal_spritelayout_null'),
              (3, 6, '255', 'bulk_terminal_spritelayout_null'),
              (3, 7, '255', 'bulk_terminal_spritelayout_null'),
    ]
)
