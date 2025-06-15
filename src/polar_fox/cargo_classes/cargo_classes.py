import os
import tomllib
from chameleon import PageTemplateLoader

# Get the directory where the current script (cargo_classes.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))


class CargoClassManager(object):

    def __init__(self):
        self.cargo_class_scheme = CargoClassScheme("cargo_classes_FIRS")

    def render_nml(self):
        # render out nml with `const foo = bar` for currend scheme
        nml_template = PageTemplateLoader(current_dir, format="text")[
            "nml_cargo_class_constants.pt"
        ]
        rendered_nml = drop_whitespace(nml_template(
            cargo_class_scheme=self.cargo_class_scheme,
        ))

        # rendered nml is written to the repo, unusual but convenient
        output_file_path = os.path.join(current_dir, "cargo_class_constants.nml")
        with open(output_file_path, "w", encoding="utf-8") as nml_file:
            nml_file.write(rendered_nml)

class CargoClassScheme(object):

    def __init__(self, scheme_name):
        self.name = scheme_name
        self.scheme_raw_config = None  # parsed later from TOML

        toml_file_path = os.path.join(current_dir, self.name + ".toml")
        with open(toml_file_path, "rb") as toml_file:
            self.scheme_raw_config = tomllib.load(toml_file)

    @property
    def cargo_classes_taxonomy(self):
        return {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "cargo_class_description" in attrs
        }

    @property
    def cargo_classes_taxonomy_by_tags(self):
        result = {}
        tags_hierarchy = {"Non-Freight": ["Passengers", "Mail"], "Freight": ["Potable Status", "Basic Handling", "Special Handling"]}
        for parent_tag, child_tags in tags_hierarchy.items():
            result[parent_tag] = {}
            for child_tag in child_tags:
                result[parent_tag][child_tag] = []
        for node_id, attrs in self.cargo_classes_taxonomy.items():
            if len(attrs["cargo_class_taxonomy_tags"]) == 2:
                parent_tag = attrs["cargo_class_taxonomy_tags"][0]
                child_tag = attrs["cargo_class_taxonomy_tags"][1]
                result[parent_tag][child_tag].append(node_id)

        return result

    @property
    def example_cargos(self):
        result = {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "cargo_description" in attrs
        }
        for node_id, attrs in result.items():
            result[node_id]["cargo_classes"] = self.sort_cargo_classes_by_taxonomy_order(attrs["cargo_classes"])
        return result

    @property
    def example_vehicles(self):
        result = {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "vehicle_description" in attrs
        }
        for node_id, attrs in result.items():
            result[node_id]["cargo_classes_allowed"] = self.sort_cargo_classes_by_taxonomy_order(attrs["cargo_classes_allowed"])
            result[node_id]["cargo_classes_disallowed"] = self.sort_cargo_classes_by_taxonomy_order(attrs["cargo_classes_disallowed"])
        return result

    @property
    def cargo_cargo_class_mapping(self):
        result = {}
        for cargo_class in self.cargo_classes_taxonomy:
            example_cargos_for_cargo_class = []
            for (
                example_cargo_node_id,
                example_cargo_attrs,
            ) in self.example_cargos.items():
                if cargo_class in example_cargo_attrs["cargo_classes"]:
                    example_cargos_for_cargo_class.append(example_cargo_node_id)
            result[cargo_class] = example_cargos_for_cargo_class
        return result

    @property
    def vehicle_cargo_class_mapping(self):
        result = {}
        for cargo_class in self.cargo_classes_taxonomy:
            example_vehicles_for_cargo_class = []
            for (
                example_vehicle_node_id,
                example_vehicle_attrs,
            ) in self.example_vehicles.items():
                if cargo_class in example_vehicle_attrs["cargo_classes_allowed"]:
                    example_vehicles_for_cargo_class.append(example_vehicle_node_id)
            result[cargo_class] = example_vehicles_for_cargo_class
        return result

    @property
    def vehicle_cargo_mapping(self):
        result = {}
        for example_cargo_node_id, example_cargo_attrs in self.example_cargos.items():
            for (
                example_vehicle_node_id,
                example_vehicle_attrs,
            ) in self.example_vehicles.items():
                disallowed_cargo = False
                for cargo_class in example_vehicle_attrs["cargo_classes_disallowed"]:
                    # first check for disallowed
                    if cargo_class in example_cargo_attrs["cargo_classes"]:
                        disallowed_cargo = True
                        # just stop checking if disallowed cargo
                        break
                if disallowed_cargo:
                    continue
                else:
                    # then check for allowed
                    for cargo_class in example_vehicle_attrs["cargo_classes_allowed"]:
                        if cargo_class in example_cargo_attrs["cargo_classes"]:
                            # quirky format where we map both cargo:vehicle and vehicle:cargo, this is unusual but makes for easy templating
                            result.setdefault(example_vehicle_node_id, []).append(
                                example_cargo_node_id
                            )
                            result.setdefault(example_cargo_node_id, []).append(
                                example_vehicle_node_id
                            )

        for k, v in result.items():
            # remove duplicates
            result[k] = list(set(v))

        return result

    def sort_cargo_classes_by_taxonomy_order(self, cargo_classes):
        # sort classes for display by class order in taxonomy (can't do this in the template, too fiddly)
        result = []
        for cargo_class in self.cargo_classes_taxonomy.keys():
            if cargo_class in cargo_classes:
                result.append(cargo_class)
        return result

def drop_whitespace(escaped_nml):
    escaped_nml = "\n".join(
        [x for x in escaped_nml.split("\n") if x.strip(" \t\n\r") != ""]
    )
    escaped_nml = "\n".join(
        [x.lstrip() for x in escaped_nml.split("\n")]
    )
    return escaped_nml

def main():
    # nothing on import, use this as a module
    pass


if __name__ == "__main__":
    main()
