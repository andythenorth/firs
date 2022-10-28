"""
FIRS does not currently generate graphics files
However there are some book-keeping tasks we perform
"""

from time import time

import firs

registered_cargos = firs.registered_cargos


def report_sprites_complete(cargos):
    # project management eh :P
    complete = len(
        [cargo.sprites_complete for cargo in cargos if cargo.sprites_complete]
    )
    for cargo in cargos:
        if cargo.sprites_complete == False:
            print(cargo.id)
    print(
        "Sprites complete for",
        complete,
        "cargos; incomplete for",
        len(cargos) - complete,
        "cargos;",
        str(int(100 * (complete / len(cargos)))) + "%",
    )


# wrapped in a main() function so this can be called explicitly, because unexpected multiprocessing fork bombs are bad
def main():
    start = time()
    print("[RENDER GRAPHICS] render_graphics.py")

    report_sprites_complete(registered_cargos)

    # eh, how long does this take anyway?
    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
