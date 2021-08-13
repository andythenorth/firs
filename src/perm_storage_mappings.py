perm_storage_mappings = {}


class PermStorageMapping(object):
    """ sparse class mapping properties names to int numbers 1-16, used to aid readability when using STORE_PERM and LOAD_PERM"""

    def __init__(self, id, identifiers):
        # doesn't need any numbers, just don't mess with positions of identifiers (or bump savegame version if you do)
        # note that OpenTTD 1.9.0 increased permanent storage to 256 registers
        if len(identifiers) > 256:
            utils.echo_message(
                "More than 256 storage identifiers passed to PermStorageMapping"
            )
        self.unused = []
        self.storage_items = {}
        for register_num, identifier in enumerate(identifiers):
            if identifier == "unused":
                self.unused.append(register_num)
            else:
                setattr(self, identifier, register_num)
                self.storage_items[identifier] = register_num
        perm_storage_mappings.setdefault(id, self)


# arguably should be in main() but eh, later (if needed)

town_perm_storage = PermStorageMapping(
    "TownStorage",
    [
        "copy_of_industry_town_count_for_debugging",
        "this_cycle_industry_counter",
        "current_optimism_score",
        "next_optimism_score",
    ],
)
