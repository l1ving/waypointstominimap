import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GdkPixbuf

w = Gdk.get_default_root_window()
sz = w.get_geometry()[2:4]
#print "The size of the window is %d x %d" % sz
pb = Gdk.pixbuf_get_from_window(w, 1783, 1064, sz[1], sz[1])
pb.savev("images/screenshot.png","png", [], [])
