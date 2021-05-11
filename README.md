# add-watermark
Application that adds a watermark to a large number of images.

```
Usage: imgwatermark.py [-h] -s SOURCE -t TARGET -w WATERMARK
                       [-p {upper_left_corner,upper_right_corner,lower_left_corner,lower_right_corner}]

Add watermarks in various positions in JPEG format.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Path of folder source
  -t TARGET, --target TARGET
                        Path of folder target
  -w WATERMARK, --watermark WATERMARK
                        Path of watermark image
  -p {upper_left_corner,upper_right_corner,lower_left_corner,lower_right_corner}, --position {upper_left_corner,upper_right_corner,lower_left_corner,lower_right_corner}
                        Position of watermark

The image used for the watermark must be 200px x 200px.
```