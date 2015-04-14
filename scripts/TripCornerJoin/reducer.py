#!/usr/bin/python

import sys
import os
from datetime import datetime

for line in sys.stdin:
	key, value = line.split("\t") 
	key = eval(key)
	value = eval(value) 

	print key, value 	
