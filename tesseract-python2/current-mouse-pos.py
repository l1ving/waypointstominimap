import pyautogui, sys

print('Press Ctrl-C to quit.')
try:
	while True:
		x, y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
		positionStr2 = '\b' * (len(positionStr) + 2)
		with open('output3.txt', 'w') as f:
			print(positionStr, file=f)
			print(positionStr2, file=f)
		sys.stdout.flush()
except KeyboardInterrupt:
	print('\n')
