import sys
import math
import random
import time

list =[]
centroid=[]
cluster=[]
oldcluster=[]
newlist=[]
newcent=[]
oldcentroid=[]
with open('km-data.txt', 'r') as my_file:
	k=int(sys.argv[2])
	method="rand"
	iteration=100
	df= sys.argv[1]
	points=my_file.readlines()
	for i in points:
		list.append(i.strip())
#choosing method rand or first
def kmeans(k,method,list,df):
	newlist=list;
	if method=="rand":
		for j in range(k):
			value=random.choice(newlist)
			centroid.append(value)
	if method=="first":
		for m in range(k):
			centroid.append(list[m])
	oldcentroid = centroid
	newcentroid = []
	print "initial centroids", centroid
	print "computing",df,"distance"
	n=0
	while(n<iteration):
		newcentroid=computecentroid(oldcentroid,list, df)
		print 'old',n, oldcentroid
		print 'new',n, newcentroid
		#checks for equality, need to do for threshold
		if oldcentroid == newcentroid:
			print 'same centroids and n = ',n
			break
		else:
			print 'different centroids, recurse again'
			oldcentroid = newcentroid
			newcentroid = []
		n= n+1
def distfunc(func, x, cx, y, cy):
	if func == "man":
		#manhattan distance
		return abs(x-cx) + abs(y-cy)
	elif func == "euc":
		#euclidean distance
		return math.sqrt((x - cx)**2 + (y - cy)**2)
	else:
		return -1
		
def computecentroid(centroid,list, df):		
	cluster=[None]*150
	for h in range(0,150):
		cluster[h]=(1000,0)

	for i in range(k):
		cvar=centroid[i]
		cx,cy=cvar.split(",")
		cxint=float(cx)
		cyint=float(cy)
		number=0
		for j in list:
			x,y=j.split(",")
			xint = float(x)
			yint = float(y)
			dist = distfunc(df,xint,cxint,yint,cyint)
			if dist < cluster[number][0]:
				cluster[number]=(dist,i+1)
			number=number+1
	newcentroid=[]
	for f in range(k):
		xsum=0.0
		ysum=0.0
		count=0
		for clusterno,items in enumerate(cluster):
			if items[1]==f+1:
				x,y=list[clusterno].split(",")
				xfloat = float(x)
				yfloat = float(y)
				count=count+1
				xsum=xsum+xfloat
				ysum=ysum+yfloat
		if count==0:
			newcentroid.append(str('0,0'))
		else:
			newcentroid.append(str(str(xsum/count)+','+str(ysum/count)))
	return newcentroid
start_time = time.time()
print kmeans(k,method,list,df)
print("--- %s seconds ---" % (time.time() - start_time))