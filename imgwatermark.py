import os
import argparse

arguments = argparse.ArgumentParser(
    description="Add watermarks in various positions and formats."
)
arguments.add_argument("-s", "--source",
                       help="Folder source", required=True)
arguments.add_argument("-t", "--target",
                       help="Folder target", required=True)
arguments.add_argument("-p", "--position",
                       help="Position of watermark", choices=[
                           "all", "upper_left_corner", "upper_right_corner", "lower_left_corner", "lower_right_corner"], default="lower_right_corner")
args = arguments.parse_args()

print(args)
