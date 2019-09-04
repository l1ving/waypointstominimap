import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GdkPixbuf
import os
import time

# select window called Go to
bashCommand = "wmctrl -a \"Go to\""
os.system(bashCommand)

# wait
time.sleep(0.08)

# screenshot
def take_screenshot(widget):
	w = Gdk.get_default_root_window()
	left, top = widget.get_position()
	width, height = widget.get_size()
	pixbuf = Gdk.pixbuf_get_from_window(w, left, top, width, height)
	return pixbuf
	print("Screenshot taken: " + path)
