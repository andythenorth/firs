from cargo_classes import CargoClassSchemes

# just a simple wrapper to render the docs on demand
# note that we intentionally include the rendered docs in the repo,
# that isn't always good practice for generated assets
# but I want the rendered html publicly available on github if the docs site disappears for any reason


def main():
    print("[CARGO CLASSES - RENDER NML CONSTANTS]")
    # note that we support rendering multiple schemes in the docs, to support comparing changes
    cargo_class_schemes = CargoClassSchemes()
    cargo_class_schemes.render_nml()
    print("[CARGO CLASSES - RENDER NML CONSTANTS] - complete")


if __name__ == "__main__":
    main()
