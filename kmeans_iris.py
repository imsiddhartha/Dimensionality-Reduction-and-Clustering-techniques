from numpy import array, dot, mean, std, empty, argsort ,size ,shape ,transpose
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
from matplotlib import pyplot as plt
import Image
import numpy as np

arr=[]
def read_ip():
	count=0
	with open('iris.data') as f:
		for line in f: # read rest of lines
			l=[]
			count=count+1
			x=line.rfind(",",0,len(line))
			l1=line[:x].split(',')
			for u in l1:
				#print u
				l.append(float(u))
		
	    		arr.append(l)
	    	#print arr
	    	#print count
	    	f.close()
	    	
def kmeans(d,m,k):
	p=0
	while 1:
		flag=0
		j=0
		
		for cell in d:
			i=0
			ind=0
			cur=0
			mini=10000
			for mean in m:
				cur=np.linalg.norm(cell[:-1]-mean)
				#print cur,i
				if cur < mini:
					ind=i
					mini=cur
				i=i+1
			#print "min is ",mini,ind	
			if d[j:j+1,len(d[0])-1] != ind:
				flag=1 
			d[j:j+1,len(data[0])-1]=ind			#4th col is for index of mean
			j=j+1
		if flag==0:
			break	
		for i in range(k):
			count=1
			mean=np.zeros((1, len(d[0])-1))
			for cell in d:
				if cell[len(d[0])-1]==i:
					mean=mean+cell[:-1]
					count=count+1
			if count !=1:
				mean=mean/count	
				m[i:i+1]=mean[:]
		p=p+1
	#print m		
	#print d
	print "No of iterations:",p
	return m,d
read_ip()    	    	    	
data= np.array(arr,float)
m = np.zeros((150, 1))
data = np.c_[data, m]		#adding a col for ith-mean
#print data
k=3
mean_mat=np.zeros((k,len(data[0])-1))
mean_mat[0:1,:]=data[0:1,:-1]
mean_mat[1:2,:]=data[50:51,:-1]
mean_mat[2:3,:]=data[100:101,:-1]
#print mean_mat


mean_mat,data=kmeans(data,mean_mat,k)

#print "final mean and data"		
#print mean_mat
#print data

conf_mat=np.zeros((3, 3))



count=0
for cell in data:
	ind=int(data[count:count+1,len(data[0])-1])
	if count<50:
		conf_mat[ind:ind+1,0]=conf_mat[ind:ind+1,0]+1
	if count > 50 and count<100:
		conf_mat[ind:ind+1,1]=conf_mat[ind:ind+1,1]+1
	if count >100 and count <150:
		conf_mat[ind:ind+1,2]=conf_mat[ind:ind+1,2]+1
	count=count+1
print "Confusion Matrix::"
print conf_mat

total=conf_mat.sum(axis=1)
#print "total"
#print total

sum1=0
print "Internal Measures:"
max_array=np.zeros((1,k))
for i in range(k):
	max_array[0,i]=max(conf_mat[i,:])
	sum1=sum1+ max(conf_mat[i,:])
#print max_array
print "parity:",sum1/len(data)	

f=0
for i in range(k):	
	fi=2*max_array[0,i]/(total[i]+50)
	f=f+fi
print "F-measure:",f/k

print "External Measures:"

win=0
wout=0
count=0
for cell in data:
	for cell1 in data:
		if cell[len(data[0])-1] == cell1[len(data[0])-1]:
			win=win+np.linalg.norm(cell[:-1]-cell1[:-1])		#sum of dist of all within same cluster,khud ka khud se 0
		if cell[len(data[0])-1] != cell1[len(data[0])-1]:			#sum of dist of all b/w same cluster
			wout=wout+np.linalg.norm(cell[:-1]-cell1[:-1]) 		
		count=count+1
win=win/2
wout=wout/2
#print win,wout
winn=0
for i in range(k):
	winn=winn+(max_array[0,i]*(max_array[0,i]-1))/2
	
n=int(k/2)
wnout=0
for i in range(n+1):
	for j in range(i,n+1):
		wnout=wnout+max_array[0,i]*max_array[0,j+1]
#print winn,wnout

betacv=(win/winn)/(wout/wnout)

print "BetaCv:",betacv

nc=1/((win/wout)+1)

print "Nc:",nc

