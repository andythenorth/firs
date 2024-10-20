import os
import tomllib
from chameleon import PageTemplateLoader

# Get the directory where the current script (cargo_classes.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))


class CargoClassSchemes(dict):
    """
    Singleton class just for ease of keeping all the schemes around easily.
    Extends default python list, as we also use it when we want a list of active rosters (the instantiated class instance behaves like a list object).
    """

    def __init__(self):
        # we support multiple schemes for the purposes of comparing them via rendered docs
        # however we only support one scheme (prod) in prod. use with grfs
        self.scheme_names = ["cargo_classes_A"]
        self.default_scheme_name = "cargo_classes_A"
        self.load_and_parse_config()

    def load_and_parse_config(self):
        # on init, load and parse TOML into a convenient structure for access
        for scheme_name in self.scheme_names:
            self[scheme_name] = CargoClassScheme(scheme_name)

    @property
    def default_scheme(self):
        return self[self.default_scheme_name]

    def render_docs(self):
        # render out docs (html currently) for all in-scope schemes
        for cargo_class_scheme in self.values():

            docs_template = PageTemplateLoader(current_dir, format="text")[
                "cargo_classes.pt"
            ]
            rendered_html = docs_template(
                cargo_class_scheme=cargo_class_scheme,
            )

            # docs are stored in the repo, as we actually want to commit them and have them available on github
            docs_dir = os.path.join(current_dir, "docs")
            output_file_path = os.path.join(docs_dir, cargo_class_scheme.name + ".html")
            with open(output_file_path, "w", encoding="utf-8") as html_file:
                html_file.write(rendered_html)


class CargoClassScheme(object):

    def __init__(self, scheme_name):
        self.name = scheme_name
        self.scheme_raw_config = None  # parsed later from TOML

        toml_file_path = os.path.join(current_dir, self.name + ".toml")
        with open(toml_file_path, "rb") as toml_file:
            self.scheme_raw_config = tomllib.load(toml_file)

    @property
    def metadata(self):
        return self.scheme_raw_config["METADATA"]

    @property
    def cargo_classes_taxonomy(self):
        return {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "cargo_class_description" in attrs
        }

    @property
    def example_cargos(self):
        result = {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "cargo_description" in attrs
        }
        return result

    @property
    def example_vehicles(self):
        result = {
            node: attrs
            for node, attrs in self.scheme_raw_config.items()
            if "vehicle_description" in attrs
        }
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
        return result


def main():
    # nothing on import, use this as a module
    pass


if __name__ == "__main__":
    main()
