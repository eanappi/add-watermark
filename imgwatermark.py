import os
import glob
import argparse
from PIL import Image

# Configure arguments of global use
arguments = argparse.ArgumentParser(
    description="Add watermarks in various positions in JPEG format.",
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
args = arguments.parse_args()

with Image.open(args.watermark) as img_file_watermark:
    # Manipulate watermark image
    img_file_watermark.convert("RGBA")
    img_file_watermark.putalpha(50)

    for file_source in glob.glob(f"{args.source}/*.jpg"):
        with Image.open(file_source) as img_file_source:
            # Split filename
            file_name, file_ext = os.path.splitext(
                os.path.split(file_source)[1])

            # Get image dimensions
            wm_size = img_file_watermark.size
            src_size = img_file_source.size

            # Calculate postiion for watermark
            wm_position = {
                "upper_left_corner": (0, 0),
                "upper_right_corner": (src_size[0] - wm_size[0], 0),
                "lower_left_corner": (0, src_size[1] - wm_size[1]),
                "lower_right_corner": (src_size[0] - wm_size[0], src_size[1] - wm_size[1])
            }

            # Add watermark image
            img_file_source.paste(img_file_watermark,
                                  wm_position[args.position], img_file_watermark)

            # Save finally image
            img_file_source.save(os.path.join(
                args.target, f"{file_name}{file_ext}"))
