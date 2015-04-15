#!/usr/bin/python

import sys
import os
import json
import csv
from scipy import spatial


master = {} 

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

def kdTreeIntersection(list_of_intersections):
    tree = spatial.KDTree(inputfile)
    return tree     

def IntersectionsMaster(tree, inputfile):
    master = {}
    f = open(fileLocation)
    reader = csv.reader(f, delimiter= ',')
    for row in reader:
        key, value = line.split('\t')
        key = eval(key)
        
        year = key[0]
        month = key[1] 

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
                master[item][year] = {}
                master[item][year][month] = 1 
            else:
                if year in master[item]:
                    if month in master[item][year]:
                        master[item][year][month] += 1
                    else:
                        master[item][year][month] = 1
                else:
                    master[item][year] = {}
                    master[item][year][month] = 1
        
    return master

if __name__ == '__main__':
    IntersectionsfileLocation = "/scratch/share/akabd/scripts/kl_scripts/TripCornerJoin/intersections.csv"
    taxipickupfilelocation = ""
    intersections = loadRoadNetwork(IntersectionsfileLocation) 
    KDtree = kdTreeIntersection(intersections)  
    intersections_dic = IntersectionsMaster(KDtree, taxipickupfilelocation)
    json_file = open('lateNightDrops_KD.json', 'w+')
    json.dump(intersections_dic, json_file)
