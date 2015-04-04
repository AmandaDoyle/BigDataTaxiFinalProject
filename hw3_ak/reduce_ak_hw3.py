#!/usr/bin/python

import sys

current_key = None
attribute_list = []
trips_list = []
fares_list = []

for line in sys.stdin:
	try:
		key, value_pair = line.strip().split("\t", 1)
		value_pair = eval(value_pair)
		table = value_pair[0]
		attributes = value_pair[1]
		key = eval(key)
	except:
		continue

	# print table
	# print attributes
	if key == current_key:
		if table == 'trips':
			trips_list = attributes
                        #print 'trips'
			#print 'trips_list'
		if table== 'fares':
			fares_list = attributes
			#print 'fares'
			#print fares_list
	
		if trips_list != [] and fares_list != []:
			attribute_list.extend(trips_list)
			attribute_list.extend(fares_list)

	else:
		if current_key:
			print "%s\t%s" %(', '.join([str(el) for el in current_key]), ', '.join([str(el) for el in attribute_list]))
		current_key = key
		if table == 'trips':
			trips_list = attributes
			fares_list = []	
		if table == 'fares':
			fares_list = attributes
			trips_list = []
		attribute_list = []
print "%s\t%s" %(', '.join([str(el) for el in current_key]), ', '.join([str(el) for el in attribute_list]))





