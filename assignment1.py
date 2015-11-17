import sys
import math
import random
list =[]
centroid=[]
cluster=[]
oldcluster=[]
newlist=[]
newcent=[]
oldcentroid=[]
with open(sys.argv[5], 'r') as my_file:
	k=int(sys.argv[1])
	method=sys.argv[2]
	threshold=float(sys.argv[3])
	iteration=int(sys.argv[4])
	
   # print(my_file.read())
	points=my_file.readlines()
	for i in points:
		list.append(i.strip())
	print list
		
#choosing method rand or first
def kmeans(k,method,list):
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
	print centroid
	n=0
	#print int('1e-9')
	while(n<iteration):
		newcentroid=computecentroid(oldcentroid,list)
		print 'old',n, oldcentroid
		print 'new',n, newcentroid
		#checks for equality, need to do for threshold
		if oldcentroid == newcentroid:
			print 'same centroids'
		else:
			print 'diff'
			oldcentroid = newcentroid
			newcentroid = []
		n= n+1
	
def computecentroid(centroid,list):		
	cluster=[None]*7
	for h in range(0,7):
		cluster[h]=(1000,0)

	for i in range(k):
		cvar=centroid[i]
		cx,cy=cvar.split(",")
		cxint=float(cx)
		cyint=float(cy)
	#print cxint,cyint
		number=0
		for j in list:
			x,y=j.split(",")
			xint = float(x)
			yint = float(y)
		#print xint,yint
			dist = math.sqrt((xint - cxint)**2 + (yint - cyint)**2)
			#print dist
			if dist < cluster[number][0]:
				cluster[number]=(dist,i+1)
			number=number+1
		#print cluster
		
		#for c,item in enumerate(cluster):
			#print c,item
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
			
	#return dist
	
print kmeans(k,method,list)
	

	
	
	
	
	
		