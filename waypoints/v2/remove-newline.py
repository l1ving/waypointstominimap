import os
import sys
import random
import re
import fileinput

for line in fileinput.input(r'/home/usr/Downloads/waypoints/small_file_1.txt', inplace = True):
	if not re.search(r'\n',line):
		print(line, end = "")