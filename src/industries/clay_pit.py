"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks, IndustryLocationChecks

industry = IndustryPrimaryExtractive(id='clay_pit',
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['CLAY'],
                    layouts='AUTO',
                    prob_in_game='4',
                    prob_random='7',
                    prod_multiplier='[16, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='46',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    # allow longer distance on clustering than usual, and more clusters, as industry is hard to locate
                    location_checks=IndustryLocationChecks(require_cluster=['clay_pit', [20, 90, 1, 4]],
                                                           incompatible={'brick_works': 16,
                                                                         'paper_mill': 16,
                                                                         'cement_plant': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_CLAY_PIT)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_PIT))',
                    fund_cost_multiplier='200',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    template="refactor_primary_waterpit.pypnml" )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

industry.add_industry_layout(
    id = 'clay_pit_layout_1',
    layout = [(0, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (2, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (3, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (4, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
              (6, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (6, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (7, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (7, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (8, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (8, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
    ]
)

industry.add_industry_layout(
    id = 'clay_pit_layout_2',
    layout = [(0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 4, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 5, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (1, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (2, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (3, 0, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 4, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 4, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 5, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 6, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
    ]
)

industry.add_industry_layout(
    id = 'clay_pit_layout_3',
    layout = [(0, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_24'),
              (0, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_18'),
              (0, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_12'),
              (0, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_6'),
              (1, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_23'),
              (1, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_17'),
              (1, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_11'),
              (1, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_5'),
              (1, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_41'),
              (1, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_37'),
              (2, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_22'),
              (2, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_16'),
              (2, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_10'),
              (2, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_4'),
              (2, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_40'),
              (2, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_36'),
              (3, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_20'),
              (3, 1, 'clay_pit_tile_1', 'clay_pit_spritelayout_14'),
              (3, 2, 'clay_pit_tile_1', 'clay_pit_spritelayout_8'),
              (3, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_2'),
              (3, 5, 'clay_pit_tile_1', 'clay_pit_spritelayout_39'),
              (3, 6, 'clay_pit_tile_1', 'clay_pit_spritelayout_35'),
              (4, 0, 'clay_pit_tile_2', 'clay_pit_spritelayout_19'),
              (4, 1, 'clay_pit_tile_2', 'clay_pit_spritelayout_13'),
              (4, 2, 'clay_pit_tile_2', 'clay_pit_spritelayout_7'),
              (4, 3, 'clay_pit_tile_2', 'clay_pit_spritelayout_1'),
    ]
)
