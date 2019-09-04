import pyautogui, sys, os

# select window called Go to
bashCommand = "wmctrl -a \"Go to\""
os.system(bashCommand)

# loop this many times
for x in range(0, 9):
	# click at x1902 y1022
	pyautogui.click(x=1902, y=1022)

