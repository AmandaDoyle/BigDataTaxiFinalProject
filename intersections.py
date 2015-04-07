import shapefile
import csv
import pyproj as pp
import sys

def convertToMap(planeVertexes):

    p0 = pp.Proj(init="esri:102718")
    f2m = 0.3048006096012192
    lngs = planeVertexes['lngs']
    lats = planeVertexes['lats']
    newPoints = []
    for i in range(len(lngs)):
        lng = lngs[i]
        lat = lats[i]

        loc = p0(f2m*lng, f2m*lat, inverse=True)
        #point = (str(loc[1]), str(loc[0]))
        point = (loc[1], loc[0])
        point = str(point)
        #print point
        newPoints.append(point)
        
    
    # print newPoints
    # print len(newPoints)
    # print len(set(newPoints))
    for point in set(newPoints):
    	point = eval(point)
    	print str(point[0]) + ' ' + str(point[1])
    #return (loc[1],loc[0])

def zipBorough(zipfile):
    with open(zipfile, 'rU') as f:
        csvReader = csv.reader(f)
        csvReader.next()
        dic = {}
        for row in csvReader:
            if 'MANHATTAN' in row[1]:
            	# print row[1]
            	# print row[0]
                dic[row[0]] = row[1]

        return dic 

    #return {row[0]:row[1] for row in csvReader if 'MAN' in row[1]}

def intersections(shapefilename, zipcodes): 

    #print dictionary
    #print 'intersections.py begin'

    dat = shapefile.Reader(shapefilename)
    record_index = 0
    list_lat = []
    list_lng = []
    lngs_to_keep = []
    lats_to_keep = []
    
    for s in dat.iterRecords():
        zipcode = s[6]
        if zipcode in zipcodes:

            shape = dat.shapeRecord(record_index).shape
            points = shape.points

            lngs = [p[0] for p in points]
            #print lngs[0]
            # lngs_to_keep.append(lngs[0])
            # lngs_to_keep.append(lngs[-1])

            lats = [p[1] for p in points]
            #print lats[0]
            # lats_to_keep.append(lats[0])
            # lats_to_keep.append(lats[-1])
        # print 'lngs'
        # print lngs
        # print 'lats' 
        # print lats

            # list_lat.extend(lats_to_keep)
            list_lng.append(lngs[0])
            list_lng.append(lngs[-1])
            list_lat.append(lats[0])
            list_lat.append(lats[-1])


            # list_lng.extend(lngs_to_keep)
        record_index+=1

    #print 'finished with intersections'
    return {'lngs': list_lng, 'lats': list_lat}

if __name__ == '__main__':
    shapefilename = sys.argv[1]
    zipfile = sys.argv[2]
    zipcodes = zipBorough(zipfile)
    lngslats = intersections(shapefilename, zipcodes)
    convertToMap(lngslats)
    #print convertToMap([1042075.132019043, 217491.56939697266])





