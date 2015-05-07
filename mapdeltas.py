import csv
import matplotlib.pyplot as plt
#%matplotlib inline

f = open('deltaswithint.csv')
#f = open('eveningdropoffschange.csv')
reader = csv.reader(f)
reader.next()
el = []
el_x = []
el_y = []
tw = []
tw_x = []
tw_y = []
th = []
th_x = []
th_y = []
for row in reader:
    if row[1] != '':
        try:
            delta = float(row[1])
            x = float(row[-1])
            y = float(row[-2])
            if delta<1:
                pass
            else:
                el_x.append(x)
                el_y.append(y) 
        except:
            continue
        el.append(delta)
        # if delta<3:
        #     el.append(1)
        # elif delta<5:
        #     el.append(5)
        # elif delta<10:
        #     el.append(10)
        # elif delta<60:
        #     el.append(40)
        # elif delta<100:
        #     el.append(50)
        # # elif delta<300:
        # #     el.append(100)
        # else:
        #     el.append(100)

    if row[2] != '':
        try:
            delta = float(row[2])
            x = float(row[-1])
            y = float(row[-2])
            if delta<1:
                pass
            else:
                tw_x.append(x)
                tw_y.append(y) 
        except:
            continue
        tw.append(delta)
        # if delta<3:
        #     tw.append(1)
        # elif delta<5:
        #     tw.append(5)
        # elif delta<10:
        #     tw.append(10)
        # elif delta<60:
        #     tw.append(40)
        # elif delta<100:
        #     tw.append(50)
        # # elif delta<300:
        # #     el.append(100)
        # else:
        #     tw.append(100)

    if row[3] != '':
        try:
            delta = float(row[3])
            x = float(row[-1])
            y = float(row[-2])
            if delta<1:
                pass
            else:
                th_x.append(x)
                th_y.append(y) 
        except:
            continue
        tw.append(delta)
        # if delta<3:
        #     th.append(1)
        # elif delta<5:
        #     th.append(5)
        # elif delta<10:
        #     th.append(10)
        # elif delta<60:
        #     th.append(40)
        # elif delta<100:
        #     th.append(50)
        # # elif delta<300:
        # #     el.append(100)
        # else:
        #     th.append(100)


    # if row[2] != '':
    #     tw.append(float(row[2]))
    #     tw_x.append(row[-1])
    #     tw_y.append(row[-2])       
    # if row[3] != '':
    #     th.append(float(row[3]))
    #     th_x.append(row[-1])
    #     th_y.append(row[-2]) 

# print len(el_x), len(el_y), len(el)
print el
print tw
print th
# print len(tw_x), len(tw_y)
# print len(th_x), len(th_y)

fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(el_x, el_y, marker = 'o', s=20, c = 'blue', alpha=0.5, edgecolors='none')
ax.scatter(tw_x, tw_y, marker = 'o', c = 'red', alpha=0.5, edgecolors='none')
ax.scatter(th_x, th_y, marker = 'o',  c = 'yellow', alpha=0.5, edgecolors='none')

# ax.scatter(el_x, el_y, s=el, marker = 'o', c = 'blue', alpha=0.5, edgecolors='none')
# ax.scatter(tw_x, tw_y, s=tw, marker = 'o',c = 'red', alpha=0.5, edgecolors='none')
# ax.scatter(th_x, th_y, s=th, marker = 'o',  c = 'yellow', alpha=0.5, edgecolors='none')

plt.show()
