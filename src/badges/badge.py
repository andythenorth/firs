import global_constants
import utils
from badges import _static_badges


# could be @dataclass but eh
class Badge(object):
    """Simple generic class for badges"""

    def __init__(self, label, **kwargs):
        self.label = label
        self.name = kwargs.get("name", None)
        self._flags = kwargs.get("flags", [])
        self.sprite = kwargs.get("sprite", None)

    @property
    def flags(self):
        result = self._flags
        if self.sprite is not None:
            result.append("BADGE_FLAG_USE_COMPANY_COLOUR")
        return ",".join(set(result))


class BadgeManager(list):
    """
    It's convenient to have a structure for working with badges.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_badge(self, label, **kwargs):
        # if not a duplicate, add the badge
        if self.get_badge_by_label(label) is None:
            self.append(Badge(label, **kwargs))
        # no return as of now, not needed

    def get_badge_by_label(self, label):
        for badge in self:
            if badge.label == label:
                return badge
        return None

    @property
    def badges_in_table_order(self):
        # 1. badge display order in OpenTTD is *not* guaranteed (as of April 2025)....so just do a basic alpha sort for now
        # 2. alpha sort is better than default append order
        # 3. alpha also makes badge order in the generated nml easier to read for debugging
        return sorted(self, key=lambda badge: badge.label)

    def render_graphics(self, iron_horse, graphics_input_path, graphics_output_path):
        badge_graphics_generator = BadgeGraphicsGenerator(
            self, iron_horse, graphics_input_path, graphics_output_path
        )
        # badge sprites may also be available from OpenTTD for some common cases
        badge_graphics_generator.render_predrawn_livery_badges()
        badge_graphics_generator.render_generated_livery_badges()

    def produce_badges(self, **kwargs):
        # explicit, not on __init__, more controllable
        self.produce_badges_from_static_config(**kwargs)
        #self.produce_power_source_badges(**kwargs)

    def produce_badges_from_static_config(self, **kwargs):
        # purely static badges
        for (
            badge_class_label,
            badge_class_properties,
        ) in _static_badges.static_badges.items():
            # first create a badge for the class
            self.add_badge(
                label=badge_class_label,
                name=badge_class_properties.get("name", None),
                sprite=badge_class_properties.get("sprite", None), # CABBAGE TEMP - unclear if this is best approach
            )
            # then create the badges for the class
            for sublabel, sublabel_properties in badge_class_properties.get(
                "sublabels", {}
            ).items():
                self.add_badge(
                    label=badge_class_label + "/" + sublabel,
                    name=sublabel_properties.get("name", None),
                    sprite=badge_class_properties.get("sprite", None), # CABBAGE TEMP - takes parent badge
                )

    """
    def produce_power_source_badges(self, **kwargs):
        for power_source in global_constants.power_sources.keys():
            self.add_badge(
                label=f"power/{power_source.lower()}",
            )
    """
