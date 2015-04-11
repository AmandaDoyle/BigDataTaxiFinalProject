#!/usr/bin/python

import sys
import os 
from datetime import datetime 

for line in sys.stdin: 
	
	line = line.strip()
	splits = line.split("\t")
	
	attributes = splits[1] 
	attributes = eval(attributes) 
		
	p0 = float(attributes[6])
	p1 = float(attributes[7])
	p2 = float(attributes[8])
	p3 = float(attributes[9])
	
	do = attributes[2]
	dt = datetime.strptime(do, '%Y-%m-%d %H:%M:%S')
	

	year = dt.year
	month = dt.month 
	day = dt.weekday()
	
	## days and hours are meant for filtering
	## not in key value output 
	hr = dt.hour	
	days = [3, 4, 5, 6]

	if p2 == 0 and p3 == 0:
		pass
	else:
		if day == 3:
			if hr >= 20:
				key = (year, month) 
				print "%s\t(%s, %s, %d)" % (key, p2, p3, 1)  
			else:
				pass
		elif day == 4 or day == 5: 
			if hr >= 0 and hr <= 3: 
				key = (year, month) 
				print "%s\t(%s, %s, %d)" % (key, p2, p3, 1)
			elif hr >= 20:
				key = (year, month) 
				print "%s\t(%s, %s, %d)" % (key, p2, p3, 1)
			else:
				pass 
		elif day == 6:
			if hr >= 0 and hr <= 3:
				key = (year, month) 
				print "%s\t(%s, %s, %d)" % (key, p2, p3, 1)
			else:
				pass
		else:
			pass 
	
	#if 3 then 20 - 23 
	#if 4 then 0 - 3 or 20 -23 
	#if 5 then 0 - 3 or 20 -23
	#if 6 0-3 
