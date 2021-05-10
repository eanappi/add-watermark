import os
import glob
import argparse
from PIL import Image

# Configure arguments of global use


def get_arguments():
    arguments = argparse.ArgumentParser(
        description="Add watermarks in various positions and formats."
    )
    arguments.add_argument("-s", "--source",
                           help="Path of folder source", required=True)
    arguments.add_argument("-t", "--target",
                           help="Path of folder target", required=True)
    arguments.add_argument("-w", "--watermark",
                           help="Path of watermark image", required=True)
    arguments.add_argument("-p", "--position",
                           help="Position of watermark", choices=[
                               "all", "upper_left_corner", "upper_right_corner", "lower_left_corner", "lower_right_corner"], default="lower_right_corner")
    return arguments.parse_args()

def manipuling_markwaterimage():
    pass

def merge_images(folder_src, folder_tar):
    pass

