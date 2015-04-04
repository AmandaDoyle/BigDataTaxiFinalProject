#!/usr/bin/python

import sys

for row in sys.stdin:
	el = row.strip().split(",")
	if len(el) == 11:
		key = el[0:4]
		attributes = el[4:]
		table = 'fares'
	else:
		key =  [el[0], el[1], el[2], el[5]]
		attributes = [el[3], el[4], el[6], el[7], el[8], el[9], el[10], el[11], el[12], el[13]]
		table = 'trips'
	value_pair = (table, attributes)
	if 'medallion' not in key:
		print "%s\t%s" % (key, value_pair)


