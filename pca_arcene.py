from numpy import array, dot, mean, std, empty, argsort ,size ,shape ,transpose
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
from matplotlib import pyplot as plt
import Image
import numpy as np
arr=[]
label=[]
def read_ip():
	count=0
	with open('train.txt') as f:
		for line in f: # read rest of lines
			
			l=[]
			count=count+1
			#x=line.rfind(" ",0,len(line))
			#l1=line[:x]
			l1=line[:].split()
			#print l1
			for u in l1:
				#print u
				l.append(float(u))
		
	    		arr.append(l)
	    	#print arr
	    	#print count
	    	f.close()
def read_label():	    	
	with open('label.txt') as f:
		for line in f: 			# read rest of lines
			label.append(float(line))
			
def pca(s,d,k,flag):
	E, V = eigh(s)				#E eigen values and V is eigen vectors	
	key = argsort(E)[::-1][:k]		#key will have indices of array
    	E, V = E[key], V[:, key]
    	V=V.transpose()
    	#print "dim of eigen vector ",V.shape
    	#print V
    	m = V[:,:]				#pc1 vs pc2
    	if k==3 and flag==0:			#pc1 vs pc3 # delete second row of C
    		print "pc1 vs pc3"
		m = np.delete(V, 1, 0)
    	if k==3 and flag==1:			#pc2 vs pc3
		print "pc2 vs pc3"
		m = np.delete(V, 0, 0)
	#print m
    	#print "dim of data vector ",data.shape
    	U = np.dot(m,data.transpose())			# U is projection matrix
    	#print "dim of Modified Data ",U.shape
    	return U


read_ip()
read_label() 	    	    	
data= np.array(arr,float)
#print data
#print label

mean_mat=mean(data,0)
#print mean_mat

temp=data-mean_mat
#print temp

scatter_mat= np.dot(temp.transpose(),temp)
print "Dim of scatter_mat"
print scatter_mat.shape


k=2
red_mat=pca(scatter_mat,data,k,0)
#print red_mat
print "Dim of Reduced_mat"
print red_mat.shape

class1=[]
class2=[]
i=0
x=red_mat.transpose()
for cell in x:
	if label[i]==-1:
		class1.append(cell)
	if label[i]==1:
		class2.append(cell)
	i=i+1
print len(class1)
#print class1

class1= np.array(class1,float)
class2= np.array(class2,float)

class1=class1.transpose()
class2=class2.transpose()

x1=class1[0:1,:]
y1=class1[1:2,:]
x2=class2[0:1,:]
y2=class2[1:2,:]

plt.scatter(x1,y1,color='red')
plt.scatter(x2,y2,color='green')

plt.show()


k=3
red_mat=pca(scatter_mat,data,k,0)
#print red_mat
print "Dim of Reduced_mat"
print red_mat.shape

class1=[]
class2=[]
i=0
x=red_mat.transpose()
for cell in x:
	if label[i]==-1:
		class1.append(cell)
	if label[i]==1:
		class2.append(cell)
	i=i+1
print len(class1)
#print class1

class1= np.array(class1,float)
class2= np.array(class2,float)

class1=class1.transpose()
class2=class2.transpose()

x1=class1[0:1,:]
y1=class1[1:2,:]
x2=class2[0:1,:]
y2=class2[1:2,:]

plt.scatter(x1,y1,color='red')
plt.scatter(x2,y2,color='green')

plt.show()
