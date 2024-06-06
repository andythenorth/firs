perm_storage_mappings = {}


def get_perm_num(identifier, industry_type=None):
    if industry_type is not None:
        if identifier in perm_storage_mappings[industry_type].storage_items.keys():
            return perm_storage_mappings[industry_type].storage_items[identifier]
    if identifier in perm_storage_mappings["town_perm_storage"].storage_items.keys():
        return perm_storage_mappings["town_perm_storage"].storage_items[identifier]
    # fall through to here if not found
    utils.echo_message("Perm storage not found for " + self.id + ": " + identifier)
    return "NOT FOUND"


def register_perm_storage_mapping(id, mapping):
    new_mapping = PermStorageMapping(id, mapping)
    perm_storage_mappings.setdefault(id, new_mapping)


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


# arguably should be in main() but eh, later

register_perm_storage_mapping(
    "town_perm_storage",
    [
        "town_industry_count_for_debugging",
        "this_cycle_industry_counter",
        "current_optimism_score",
        # next_optimism_score is not required
        "current_basic_needs_and_luxuries_score",
        "next_basic_needs_and_luxuries_score",
        "current_pollution_and_squalor_score",
        "next_pollution_and_squalor_score",
    ],
)
