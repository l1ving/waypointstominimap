import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GdkPixbuf
import os
import time
import sys
import keyboard
import subprocess
import pyautogui
	
# loop this many times
for x in range(0, 20):

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
	
	# run tesseract from bash
	bashCommand = "tesseract active.png stdout >> output1.txt"
	os.system(bashCommand)
	
	# wait
	time.sleep(1.3)
	
	# grab window title
	command = "xprop -root _NET_ACTIVE_WINDOW"
	frontmost = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8").strip().split()[-1]
	## print(frontmost)
	
	# correct ID
	fixed_id = frontmost[:2]+"0"+frontmost[2:]
	## print(fixed_id)
	
	# grab window title
	command = "wmctrl -lp"
	window_pid = [l.split()[2] for l in subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8").splitlines() if fixed_id in l][0]
	## print(window_pid)
	
	# debugging to test if it works
	## if ( window_pid == "2375" ):
		## print("Code will work")
	## else:
		## print("your code is shitty and doesn't work")
	
	# actually run function
	## if ( window_pid == "2375" ):
		# select window called Go to
	bashCommand = "python3 press-buttons.py >> output4.txt"
	os.system(bashCommand)
	
	## else:
		## print("you're retarded and this doesn't work")
	
	# loop this many times
	for x in range(0, 9):
		# click at x1902 y1022
		pyautogui.click(x=1902, y=1022)
