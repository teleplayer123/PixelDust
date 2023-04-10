from utils.utils import convert_pixel_type, threshold_image_gs
from capture.frame_cap import screenshot_bmp

fn = screenshot_bmp()
new_fn = convert_pixel_type(fn, "convert_image.jpg", "bgr", "rgb")
new_fn_thresh = threshold_image_gs(new_fn, "binary")