#!/usr/bin/python

import sys
import os
from datetime import datetime
import csv
from scipy import spatial


fileLocation = ""

def loadRoadNetwork(fileLocation):
	f = open(fileLocation)
	reader = csv.reader(f, delimiter= ',')
	list_of_intersections = []  
	
	for l in reader:
		try:
			point = [float(l[1]), float(l[0])]
			list_of_intersections.append(point)
		except:
			pass 
	return list_of_intersections 	

intersections = loadRoadNetwork(fileLocation) 

def kdTreeIntersection(inputfile):
	tree = spatial.KDTree(inputfile)
	return tree 	

tree = kdTreeIntersection(intersections)  

master = {} 

for line in sys.stdin:

	key, value = line.split('\t')
	
	key = eval(key)
	
	#year = key[0]
	#month = key[1] 

	value = eval(value) 
	
	lat = float(value[0])
	lng = float(value[1]) 
		
	loc = [] 
	loc.append(lat)
	loc.append(lng) 

	ind = tree.query_ball_point(loc, .001)

	for item in ind:
		if item not in master:
			master[item] = {} 
			master[item][key] = 1 
		else:
			if key in master[item]:
				master[item][key] += 1
			else:
				master[item][key] = 1 
	
for item in master.items():
	print item


