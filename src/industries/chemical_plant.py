"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='chemical_plant',
                    processed_cargos_and_output_ratios=[('OIL_', 6), ('NITR', 6)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['RFPR'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='191',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'chemical_plant': 56,
                                                                         'oil_wells': 16,
                                                                         'nitrate_mine': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_CHEMICAL_PLANT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='170',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    extra_text_industry='STR_EXTRA_CHEMICAL_PLANT' )

industry.economy_variations['BASIC_TROPIC'].enabled = True

industry.add_tile(id='chemical_plant_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))
industry.add_tile(id='chemical_plant_tile_2',
                  animation_length=47,
                  animation_looping=True,
                  animation_speed=2,
                  custom_animation_control={'macro':'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'chemical_plant_spriteset_ground',
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'chemical_plant_spriteset_ground_overlay',
    type='empty',
)

spriteset_horizontal_tanks = industry.add_spriteset(
    id = 'chemical_plant_spriteset_horizontal_tanks',
    sprites = [(150, 10, 64, 114, -31, -83)],
    zextent = 60
)
spriteset_frac_columns = industry.add_spriteset(
    id = 'chemical_plant_spriteset_frac_columns',
    sprites = [(220, 10, 64, 114, -31, -83)],
    zextent = 95
)
spriteset_drop_tower_and_thin_chimney = industry.add_spriteset(
    id = 'chemical_plant_spriteset_drop_tower_and_thin_chimney',
    sprites = [(290, 10, 64, 114, -31, -83)],
    zextent = 127
)
spriteset_large_building = industry.add_spriteset(
    id = 'chemical_plant_spriteset_large_building',
    sprites = [(360, 10, 64, 114, -31, -83)],
    zextent = 70
)
spriteset_fat_chimney = industry.add_spriteset(
    id = 'chemical_plant_spriteset_fat_chimney',
    sprites = [(430, 10, 64, 114, -31, -83)],
    zextent = 90
)
spriteset_spherical_tanks = industry.add_spriteset(
    id = 'chemical_plant_spriteset_spherical_tanks',
    sprites = [(500, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_vertical_tanks = industry.add_spriteset(
    id = 'chemical_plant_spriteset_vertical_tanks',
    sprites = [(570, 10, 64, 66, -31, -35)],
    zextent = 48
)
spriteset_barrels = industry.add_spriteset(
    id = 'chemical_plant_spriteset_barrels',
    sprites = [(710, 10, 64, 66, -31, -35)],
    zextent = 48
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset = 0,
    yoffset = 0,
    zoffset = 81,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 6,
    yoffset = -1,
    zoffset = 45,
)
sprite_smoke_3 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 6,
    yoffset = 3,
    zoffset = 45,
)
sprite_smoke_4 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 2,
    yoffset = -1,
    zoffset = 45,
)
sprite_smoke_5 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 2,
    yoffset = 3,
    zoffset = 45,
)
sprite_smoke_6 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 6,
    yoffset = 0,
    zoffset = 60,
)
sprite_smoke_7 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 6,
    yoffset = 3,
    zoffset = 60,
)
sprite_smoke_8 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 3,
    yoffset = 0,
    zoffset = 60,
)
sprite_smoke_9 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset = 3,
    yoffset = 3,
    zoffset = 60,
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_horizontal_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_horizontal_tanks],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_frac_columns',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_frac_columns],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_drop_tower_and_thin_chimney',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_drop_tower_and_thin_chimney],
    smoke_sprites = [sprite_smoke_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_large_building',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_large_building],
    smoke_sprites = [sprite_smoke_2, sprite_smoke_3, sprite_smoke_4, sprite_smoke_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_fat_chimney',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_fat_chimney],
    smoke_sprites = [sprite_smoke_6, sprite_smoke_7, sprite_smoke_8, sprite_smoke_9],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_spherical_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_spherical_tanks],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_vertical_tanks',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_vertical_tanks],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'chemical_plant_spritelayout_barrels',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_barrels],
    fences = ['nw','ne','se','sw']
)


industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_1',
    layout = [(0, 0, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (0, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (1, 0, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (1, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (3, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (3, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_drop_tower_and_thin_chimney'),
              (4, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (4, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_2',
    layout = [(0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_drop_tower_and_thin_chimney'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (1, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (1, 3, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 3, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_3',
    layout = [(0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_drop_tower_and_thin_chimney'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (1, 2, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (1, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 2, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (2, 3, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_4',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (1, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (3, 0, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (3, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (4, 0, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (4, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (5, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_drop_tower_and_thin_chimney'),
              (5, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (6, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (6, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
    ]
)
industry.add_industry_layout(
    id = 'chemical_plant_industry_layout_5',
    layout = [(0, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_drop_tower_and_thin_chimney'),
              (0, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (0, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_vertical_tanks'),
              (1, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_frac_columns'),
              (1, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (1, 2, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_fat_chimney'),
              (2, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (2, 1, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (2, 2, 'chemical_plant_tile_2', 'chemical_plant_spritelayout_large_building'),
              (3, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_horizontal_tanks'),
              (3, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (3, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
              (4, 0, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (4, 1, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_spherical_tanks'),
              (4, 2, 'chemical_plant_tile_1', 'chemical_plant_spritelayout_barrels'),
    ]
)
