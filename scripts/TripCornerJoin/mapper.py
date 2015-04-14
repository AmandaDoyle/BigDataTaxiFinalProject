#!/usr/bin/python

import sys
import os
from datetime import datetime
import csv
from scipy import spatial


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

def kdTreeIntersection(inputfile):
	tree = spatial.KDTree(inputfile)
	return tree

def parseIndices(y, m, list):
	for i in list: 
		key = (y, m, i) 
		val = 1 
		print "%s\t%d" % (key, val) 

def parseInput():
	for line in sys.stdin:
		line = line.strip()
		splits = line.split("\t")
		attributes = splits[1]
		attributes = eval(attributes)
		
		yield attributes 
					
def mapper():
	for values in parseInput():
		try:
			p2 = float(values[8])
			p3 = float(values[9])
			loc = [] 	
			loc.append(p2)
			loc.append(p3) 	
			dropoff = values[2]
			dt = datetime.strptime(dropoff, '%Y-%m-%d %H:%M:%S')
			year = dt.year
			month = dt.month
			day = dt.weekday()
			hr = dt.hour 
		except:
			pass 
		
		if p2 == 0 and p3 == 0:
			pass
		else:
			if day == 3:
				if hr >= 20:
					#print year, month, p2, p3
					ind = tree.query_ball_point(loc, .001)
					parseIndices(year, month, ind) 
				else:
					pass
			elif day == 4 or day == 5:
				if hr >= 0 and hr <= 3:
					ind = tree.query_ball_point(loc, .001)
					parseIndices(year, month, ind)
				elif hr >= 20:
					ind = tree.query_ball_point(loc, .001)
					parseIndices(year, month, ind) 
				else:
					pass
			elif day == 6:
				if hr >= 0 and hr <= 3:
					ind = tree.query_ball_point(loc, .001)
					parseIndices(year, month, ind)
				else:
					pass
			else:
				pass
	
		
if __name__=='__main__':
	fileLocation = "intersections.csv" 
	intersections = loadRoadNetwork(fileLocation)
	tree = kdTreeIntersection(intersections)
	mapper() 
