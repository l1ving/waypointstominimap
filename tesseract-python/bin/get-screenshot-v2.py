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

# screenshot active window
screen = Gdk.get_default_root_window().get_screen()
w = screen.get_active_window()
pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
pb.savev("active.png", "png", (), ())
