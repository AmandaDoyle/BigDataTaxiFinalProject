import shapefile
import csv

import pyproj as pp
p0 = pp.Proj(init="esri:102718")
f2m = 0.3048006096012192

def convertToMap(planeVertex):
    loc = p0(f2m*planeVertex[0], f2m*planeVertex[1], inverse=True)
    lat = round(loc[1], 5)
    lng = round(loc[0], 5)
    return (lat, lng)
    #return (loc[1],loc[0])

shapefilename = sys.argv[0]
dat = shapefile.Reader(shapefilename)

sr = dat.shapeRecords()

dict = {} 
index = 0 

for item in sr:
	street = sr[index].shape.points
	p1 = convertToMap(street[0])
	p2 = convertToMap(street[1])
		
	if p1 in dict: 
		dict[p1] += 1
	else:
		dict[p1] = 1

	if p2 in dict:
		dict[p2] += 1 
	else:
		dict[p2] = 1 
		
	index += 1 

for item in dict.items():
	if item[1] == 1:
		del dict[item[0]]
	else:
		pass 

with open('new.csv', 'wb') as write_file:
	file_writer = csv.writer(write_file)
	for i in dict.items():
		file_writer.writerow(i[0])




