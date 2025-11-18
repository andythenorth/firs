class GRFObject(object):
    """Stubby class to hold objects - GRFObject to avoid conflating with built-in python classname"""

    def __init__(self, industry, add_to_object_num, **kwargs):
        # note spacing numeric part of id to add a leading 0 if needed, otherwise python lexical sort returns 'foo_1, foo_10, foo_2' etc
        self.id = f"{industry.id}_object_{add_to_object_num:02}"
        # we allocate up a range of up to 100 object numeric IDs per industry, using the industry numeric ID
        # this will keep object IDs relatively stable across releases unless the industry numeric ID changes or add_to_object_num changes
        if add_to_object_num > 99:
            raise BaseException(
                "Industry "
                + industry.id
                + " defines an object with numeric ID "
                + str(add_to_object_num)
                + " which exceeds the limit of 99"
            )
        self.numeric_id = (industry.numeric_id * 100) + add_to_object_num
        self.views = []
        self.industry = industry
        # default to allowing both land and water, suppress explicitly when necessary
        self.allow_on_land = kwargs.get("allow_on_land", True)
        self.allow_on_water = kwargs.get("allow_on_water", True)

    def add_view(self, spritelayout):
        self.views.append(spritelayout)
        # self.validate()

    def validate(self):
        # must be 1, 2, or 4 views https://newgrf-specs.tt-wiki.net/wiki/NML:Objects#Location_check_results
        if len(self.views) == 3:
            raise BaseException(
                self.id, "has 3 views defined, which is not permitted by spec"
            )
        # validation for case of too many views - shouldn't happen but eh
        if len(self.views) > 4:
            raise BaseException(f"{self.id} has too many views defined \n {self.views}")

    @property
    def tile(self):
        # all views in the object must resolve to one and only one industry tile
        # we use this for certain object properties / callbacks (such as animation, and possibly location checks)
        # check for mismatched tiles
        found_tiles = []
        for view in self.views:
            for x, y, spritelayout in view:
                found_tiles.append(spritelayout.resolve_tile(self.industry))
        if len(set(found_tiles)) != 1:
            raise BaseException(self.id, "tiles don't match:", found_tiles)
        else:
            # we have one and only one tile
            return found_tiles[0]

    @property
    def multi_tile_ground(self):
        result = []
        # only one view supported currently for multi_tile objects (could do more, but just 1 currently for basic simplicity)
        for x, y, spritelayout in self.views[0]:
            result.append([x, y, spritelayout.ground_sprite])
        return result

    @property
    def multi_tile_buildings(self):
        result = []
        # only one view supported currently for multi_tile objects (could do more, but just 1 currently for basic simplicity)
        for x, y, spritelayout in self.views[0]:
            for building_sprite in spritelayout.building_sprites:
                result.append([x, y, building_sprite])
        return result

    @property
    def object_flags(self):
        tile_type_flags = []
        if self.allow_on_land == False:
            tile_type_flags.append("OBJ_FLAG_NOT_ON_LAND")
        if self.allow_on_water:
            tile_type_flags.append("OBJ_FLAG_ON_WATER")
        return f"bitmask(OBJ_FLAG_ANYTHING_REMOVE, OBJ_FLAG_ANIMATED, OBJ_FLAG_ON_WATER, {",".join(tile_type_flags)})"

    @property
    def animation_triggers(self):
        # object animation triggers don't match industry tile triggers, so remap
        result = []
        trigger_remap = {
            "ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE": "ANIM_TRIGGER_OBJ_BUILT",
            "ANIM_TRIGGER_INDTILE_TILE_LOOP": "ANIM_TRIGGER_OBJ_TILELOOP",
        }
        # split off some nml formatting to get the raw list
        triggers = (
            self.tile.animation_triggers.split("bitmask(")[1].split(")")[0].split(",")
        )
        # triggers from tile might be empty, strip those
        triggers = [i for i in triggers if i != ""]
        # this is expected to error if the trigger isn't found, it only mapped the triggers in use as of September 2022, not all possible triggers
        for trigger in triggers:
            result.append(trigger_remap[trigger])
        return "bitmask(" + ",".join(result) + ")"

    @property
    def size(self):
        view_sizes = []
        for view in self.views:
            x_values = [i[0] for i in view]
            y_values = [i[1] for i in view]
            view_size = (max(x_values), max(y_values))
            view_sizes.append(view_size)
        unique_sizes = list(set(view_sizes))
        if len(unique_sizes) > 1:
            raise BaseException(self.id, "views have different sizes / tile layouts")
        return [1 + unique_sizes[0][0], 1 + unique_sizes[0][1]]


