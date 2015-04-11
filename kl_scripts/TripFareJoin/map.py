#!/usr/bin/python

import sys
import os

for line in sys.stdin:
		
	line = line.strip() 
	splits = line.split(",")

	if len(splits) == 11: 
		
		key1 = splits[0]
		key2 = splits[1]
		key3 = splits[2]
		key4 = splits[3]
		keyAttributes = (key1, key2, key3, key4)
 
		otherAttributes = ",".join(splits[4:]) 		
		
		valuePair = ("fares", otherAttributes) 
		
		if key1 != 'medallion': 
			print "%s\t%s" % (keyAttributes, valuePair) 
		else:
			pass		

	elif len(splits) == 14:
		
		key1 = splits[0]
		key2 = splits[1]
		key3 = splits[2]
		key4 = splits[5]
		keyAttributes = (key1, key2, key3, key4)			

		other1 = ",".join(splits[3:5])
		other2 = ",".join(splits[6:])
		otherAttributes = other1 + "," + other2
		valuePair = ("trips", otherAttributes) 	
		
		if key1 != 'medallion':
			print "%s\t%s" % (keyAttributes, valuePair)
		else:
			pass

	else:
		pass

