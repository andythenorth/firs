"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

from PIL import Image, ImageDraw
from copy import deepcopy
import os.path

currentdir = os.curdir


class Spritesheet:
    """
    Class holding the sprite sheet.

    @ivar sprites: The sprite sheet.
    @type sprites: L{Image}
    """

    def __init__(self, width, height, palette):
        """
        Construct an empty sprite sheet.

        @param width: Width of the sprite sheet.
        @type  width: C{int}

        @param height: Height of the sprite sheet.
        @type  height: C{int}

        @param palette: Palette of the sprite sheet.
        @type  palette: C{list} of (256*3) C{int}
        """
        self.sprites = Image.new("P", (width, height), 255)
        self.sprites.putpalette(palette)

    def save(self, output_path):
        self.sprites.save(output_path, optimize=True)


class PieceCargoSprites:
    """
    Convenience class to hold sprites for piece cargos, sliced up by angle
    """

    def __init__(self, polar_fox_constants, polar_fox_graphics_path):
        # note that specific polar_fox attributes *must* be passed explicitly
        # can't just pass polar_fox module as it's not always in scope
        # similarly the path to polar fox graphics must be set explicitly as it varies by scope
        self.polar_fox_constants = polar_fox_constants
        self.sprites_by_filename = {}
        # it may be undesirable for performance reasons to slice all the sprites on init, but I think we can chance it eh?
        for (
            cargo_filename
        ) in self.polar_fox_constants.piece_sprites_to_cargo_labels_maps.keys():
            cargo_sprites_input_path = os.path.join(
                currentdir,
                polar_fox_graphics_path,
                "piece_cargos",
                cargo_filename + ".png",
            )
            cargo_sprites_input_image = Image.open(cargo_sprites_input_path)
            self.sprites_by_filename[cargo_filename] = cargo_sprites_input_image.copy()
            # don't leave open files around, it can hit open file limits on macOs, maybe elsewhere; we've copied the Image object above to avoid needing the file handle
            cargo_sprites_input_image.close()

    def get_cargo_sprites_all_angles_for_length(self, cargo_filename, length):
        # provide a list, with a two-tuple (cargo_sprite, mask) for each of 4 angles
        # cargo sprites are assumed to be symmetrical, only 4 angles are needed
        # cargos with 8 angles (e.g. bulldozers) aren't supported, use a different gestalt & template for those (dedicated or custom)
        # loading states are first 4 sprites, loaded are second 4, all in one list, just pick them out as needed
        return get_arbitrary_angles(
            self.sprites_by_filename[cargo_filename],
            self.cargo_spritesheet_bounding_boxes[length],
        )

    @property
    def cargo_spritesheet_bounding_boxes(self):
        # Cargo spritesheets provide multiple lengths, using a specific format of rows
        # given a base set, find the bounding boxes for the rows per length
        cargo_spritesheet_bounding_boxes = {}
        for counter, length in enumerate([3, 4, 5, 6, 7, 8]):
            bb_result = []
            for y_offset in [0, 30]:
                bb_y_offset = (counter * 60) + y_offset
                bb_result.extend(
                    tuple(
                        [
                            (i[0], i[1] + bb_y_offset, i[2], i[3] + bb_y_offset)
                            for i in self.polar_fox_constants.cargo_spritesheet_bounding_boxes_base
                        ]
                    )
                )
            cargo_spritesheet_bounding_boxes[length] = bb_result
        return cargo_spritesheet_bounding_boxes


def get_arbitrary_angles(input_image, bounding_boxes):
    # given an image and a list of arbitrary bounding boxes...
    # ...return a list of two tuples with sprite and mask
    # this can then be used for compositing
    # note the arbitrary order of sprites which makes this very flexible
    result = []
    for bounding_box in bounding_boxes:
        sprite = input_image.copy()
        sprite = sprite.crop(bounding_box)
        mask = sprite.copy()
        # !! .point is noticeably slow although not signifcantly so with only 3 cargo types
        # !! check this again if optimisation is a concern - can cargos be processed once and passed to the pipeline?
        # !! as of Oct 2018, I tested commenting out *all* piece cargo processing, including calls to this method
        # !! that cut only 1s from an 11s graphics processing run on single CPU
        # !! so optimising this is TMWFTLB currently; instead simply using multiprocessing cuts graphics run to 2s
        mask = mask.point(lambda i: 0 if i == 0 else 255).convert("1")
        result.append((sprite, mask))
    return result


def make_cheatsheet(image, output_path, origin=None):
    block_size = 30
    palette = deepcopy(image.palette)
    rawpx = image.load()
    result = Image.new("P", (image.size[0] * block_size, image.size[1] * block_size))
    result.putpalette(palette)
    draw = ImageDraw.Draw(result)

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pen_x = x * block_size
            pen_y = y * block_size
            colour = rawpx[x, y]
            draw.rectangle(
                [(pen_x, pen_y), (pen_x + block_size, pen_y + block_size)], fill=colour
            )
            if origin is not None and (x, y) == origin:
                # indicate origin; hacky, can't be bothered to learn to draw lines, so just draw more rects :P
                draw.rectangle(
                    [(pen_x, pen_y), (pen_x + block_size, pen_y + block_size)], fill=224
                )
                draw.rectangle(
                    [
                        (pen_x + 3, pen_y + 3),
                        (pen_x + block_size - 4, pen_y + block_size - 4),
                    ],
                    fill=colour,
                )
            bg_size = draw.textsize(str(colour))
            text_pos_x = pen_x + 0.75 * block_size - bg_size[0]
            text_pos_y = pen_y + block_size // 3
            draw.rectangle(
                [
                    (text_pos_x - 1, text_pos_y + 1),
                    (text_pos_x + bg_size[0], text_pos_y + bg_size[1] - 2),
                ],
                fill=255,
            )
            draw.text((text_pos_x, text_pos_y), str(colour), fill=1)

    result.save(output_path, optimize=True)


def make_spritesheet_from_image(input_image, palette):
    # convenience method to get a spritesheet from a passed PIL image
    spritesheet = Spritesheet(
        width=input_image.size[0], height=input_image.size[1], palette=palette
    )
    spritesheet.sprites.paste(input_image)
    return spritesheet


def pixascan(image):
    """
    Optimisation method: scans an image from top left, rows first, and caches
    significant pixels from it into a list for reuse in multiple render passes.

    @param image: Source image.
    @type  image: L{PIL.Image}

    @return: Significant pixels in the image (top-left to bottom-right, rows first).
    @rtype:  A C{list} of C{tuple} (x, y, colour)
    """
    significant_pixels = []
    imagepx = image.load()
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            colour = imagepx[x, y]
            if colour not in (0, 255):  # don't store white, blue; assumes DOS palette
                significant_pixels.append((x, y, colour))
    return significant_pixels
