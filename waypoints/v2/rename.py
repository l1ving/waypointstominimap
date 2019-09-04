import os
import sys
import random
import re

if sys.version_info[0] != 3 or sys.version_info[1] < 0:
	print("This script requires Python version 3.0")
	sys.exit(1)

for x in range(0, 1000):	
	# list out files
	fileList = ['zzz_split_19.txt', 'zzz_split_3.txt', 'zzz_split_78.txt']
	
	# define the current file as a random choice
	currentfile = random.choice(fileList)
	print(currentfile)

	# define this
	#convertedname = "'" + currentfile + "', "
	#print(convertedname)

	# open current file and read first line
	with open(currentfile) as f:
		first_line = f.readline()
		first_line = first_line.rstrip()

	# define fullnamejson as END + first_line + .json
	fullnamejson = "END_" + first_line + ".json"

	# define fullname as END + first_line
	fullname = "END_" + first_line

	os.rename(currentfile, fullnamejson)
	print(fullnamejson)

	# define x y and z
	x, y, z =first_line.split(',')

	# define formatted as what will be written to the file
	formatted = "{\n  \"id\": \"" + fullname + "\",\n  \"name\": \"END\",\n  \"icon\": \"waypoint-normal.png\",\n  \"x\": " + x + ",\n  \"y\": " + y + ",\n  \"z\": " + z + ",\n  \"r\": 61,\n  \"g\": 1,\n  \"b\": 164,\n  \"enable\": true,\n  \"type\": \"Normal\",\n  \"origin\": \"journeymap\",\n  \"dimensions\": [\n    0\n  ],\n  \"persistent\": true\n}"
	print(formatted)

	# write to file
	with open(fullnamejson, "w") as text_file:
		##print(f(fullnamejson), file=text_file)
		print(f'{formatted}', file=text_file)
