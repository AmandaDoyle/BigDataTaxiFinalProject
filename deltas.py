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

def calcDeltas(master):
    year_change = {}
    total_change = {}

    years = [2010, 2011, 2012, 2013]

    for int_index, v in master.items():
        deltas = []
        for i in range(len(years)-1):
            try:
                if years[i] in v and years[i+1] in v:
                    if v[years[i]]['total'] != 0:
                        delta = float((v[years[i+1]]['total']-v[years[i]]['total'])/v[years[i]]['total'])
                    else:
                        delta = 0
                    deltas.append(delta)

            except ValueError:
                deltas.append(0)
        year_change[int_index] = deltas
    
    for k, v in year_change.items():
        try: 
            total_change[k] = float(float(sum(v))/len(v))
        except:
            continue

    top_change = sorted(total_change.items(), key = lambda x: (-x[1], x[0]))
    print top_change
        

if __name__ == '__main__':

    intersections_dic = IntersectionsMaster()

    #json_file = open('', 'w+')
    #json.dump(intersections_dic, json_file)
    calcDeltas(intersections_dic)








