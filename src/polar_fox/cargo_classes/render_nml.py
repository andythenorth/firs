from cargo_classes import CargoClassManager

# just a simple wrapper to render the nml constants on demand
# note that we intentionally include the nml constants file in the repo,
# that isn't always good practice for generated assets
# but I want the assets publicly available on github if the docs site disappears for any reason


def main():
    print("[CARGO CLASSES - RENDER NML CONSTANTS]")
    cargo_class_manager = CargoClassManager()
    cargo_class_manager.render_nml()
    print("[CARGO CLASSES - RENDER NML CONSTANTS] - complete")


if __name__ == "__main__":
    main()
