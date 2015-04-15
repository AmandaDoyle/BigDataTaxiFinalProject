#!/usr/bin/python

import sys
import os
import json
import csv

def IntersectionsMaster():
	master = {}
	for line in sys.stdin:
        key, value = line.strip().split('\t')
        try: 
        	key = eval(key)
	        
	        year = key[0]
	        month = key[1] 
	        int_index = key[2]
	        count = int(value)

	    except:
	    	continue

	    if int_index not in master:
	    	master[int_index] = {}
	    	master[int_index][year] = {}
            master[int_index][year][month] = count
            master[int_index][year]['total'] = count
        else:
        	if year not in master[int_index]:
        		master[int_index][year] = {}
                master[int_index][year][month] = count
            	master[int_index][year]['total'] = count
            else:
            	#first if just in case shuffle/sort didn't work as expected and not all months are aggregated
            	if month in master[int_index][year]:
            		master[int_index][year][month] += count
            		master[int_index][year]['total'] += count
            	
            	else:
                    master[int_index][year][month] = count
            	    master[int_index][year]['total'] += count
    
    return master

def year_change(master):
    
    year_change = {}
    total_change = {}

    for int_index in master:
   


    	



if __name__ == '__main__':

    intersections_dic = IntersectionsMaster()

    json_file = open('', 'w+')
    json.dump(intersections_dic, json_file)








