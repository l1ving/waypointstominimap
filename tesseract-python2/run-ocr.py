import os
import sys

# run tesseract from bash
bashCommand = "tesseract active.png stdout >> output1.txt"
os.system(bashCommand)
