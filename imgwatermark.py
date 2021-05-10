import os
import glob
import argparse
from PIL import Image

# Configure arguments of global use


def get_arguments():
    arguments = argparse.ArgumentParser(
        description="Add watermarks in various positions and formats.",
        epilog="The image used for the watermark must be 200px x 200px."
    )
    arguments.add_argument("-s", "--source",
                           help="Path of folder source", required=True)
    arguments.add_argument("-t", "--target",
                           help="Path of folder target", required=True)
    arguments.add_argument("-w", "--watermark",
                           help="Path of watermark image", required=True)
    arguments.add_argument("-p", "--position",
                           help="Position of watermark", choices=[
                               "upper_left_corner", "upper_right_corner", "lower_left_corner", "lower_right_corner"], default="lower_right_corner")
    return arguments.parse_args()


def merge_images(img_source, img_watermark, watermark_pos):
    # Get size from img_source
    img_source_size = img_source.size
    img_watermark_size = img_watermark.size

    # Dictionary with calculate positions
    watermark_corner = {
        "upper_left_corner": (0, 0),
        "upper_right_corner": (img_source_size[0] - img_watermark_size[0], 0),
        "lower_left_corner": (0, img_source_size[1] - img_watermark_size[1]),
        "lower_right_corner": (img_source_size[0] - img_watermark_size[0], img_source_size[1] - img_watermark_size[1])
    }

    # Paste watermark on first image
    img_source.paste(img_watermark, watermark_corner[pos_watermark])

    return img_source


with Image.open(get_arguments().watermark) as img_file_watermark:
    for image_file in glob.glob(f"{get_arguments().source}/*.jpg"):
        with Image.open(os.path.join(get_arguments().source, image_file)) as img_file_source:
            merge_image = merge_images(img_file_source, img_file_watermark,
                                       get_arguments().position)
            merge_image.save(os.path.join(get_arguments().target, image_file))
