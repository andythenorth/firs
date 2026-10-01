"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

class Vulcan(object):
    """Used for GS configuration at compile time, which influences GS at run time"""

    def __init__(self, industry):
        self.industry = industry

    @property
    def default_vulcan_config(self):
        # CABBAGE unclear why vulcan_config was fetched but not used
        # vulcan_config = self.industry.get_property("vulcan_config", None)
        result = {}
        result["allow_production_change_from_gs"] = getattr(
            self.industry, "allow_production_change_from_gs", False
        )
        # append some additional derived properties to Vulcan config
        result["town_cargo_sink_industry"] = (
            True
            if self.industry.id in ["builders_yard", "hardware_store", "general_store"]
            else False
        )
        return result

    @property
    def economy_variations(self):
        result = {}
        for economy in self.industry.economies_enabled_for_industry:
            economy_config = {}
            economy_config["accept_cargo_types"] = (
                self.industry.get_accepted_cargo_labels_by_economy(economy)
            )
            economy_config["vulcan_config"] = self.industry.get_property(
                "vulcan_config", economy
            )
            result[economy.id] = economy_config
        return result
