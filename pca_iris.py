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
			#l1=line[:x]
			l1=line[:x].split(',')
			#print l1
			for u in l1:
				#print u
				l.append(float(u))
		
	    		arr.append(l)
	    	#print arr
	    	#print count
	    	f.close()   	   
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
    	return U,V


read_ip()    	    	    	
data= np.array(arr,float)
#print data
mean_mat=mean(data,0)
#print mean_mat

temp=data-mean_mat
#print temp

scatter_mat= np.dot(temp.transpose(),temp)
print "Dim of scatter_mat"
print scatter_mat.shape
#print np.var(data)
#print 150*scatter_mat
k=2
red_mat,V=pca(scatter_mat,data,k,0)
#print red_mat
print "Dim of Reduced_mat"
print red_mat.shape
x201=red_mat[0:1,0:50]
x202=red_mat[0:1,50:100]
x203=red_mat[0:1,100:150]
y201=red_mat[1:2,0:50]
y202=red_mat[1:2,50:100]
y203=red_mat[1:2,100:150]

#print np.var(red_mat.transpose())
#print V.shape,scatter_mat.shape
#print np.dot(np.dot(V,scatter_mat),V.transpose())

plt.scatter(x201,y201,color='red',label="Iris-setosa")
plt.scatter(x202,y202,color='green',label="Iris-versicolor")
plt.scatter(x203,y203,color='yellow',label="Iris-virginica")
plt.legend()
plt.title('Pc1 Vs Pc2')
plt.show()

k=3
red_mat,V=pca(scatter_mat,data,k,0)
#print red_mat
print "Dim of Reduced_mat"
print red_mat.shape

x201=red_mat[0:1,0:50]
x202=red_mat[0:1,50:100]
x203=red_mat[0:1,100:150]
y201=red_mat[1:2,0:50]
y202=red_mat[1:2,50:100]
y203=red_mat[1:2,100:150]

#print np.var(red_mat.transpose())
plt.scatter(x201,y201,color='red',label="Iris-setosa")
plt.scatter(x202,y202,color='green',label="Iris-versicolor")
plt.scatter(x203,y203,color='yellow',label="Iris-virginica")
plt.legend()
plt.title('Pc1 Vs Pc3')
plt.show()


k=3
red_mat,v=pca(scatter_mat,data,k,1)
#print red_mat
print "Dim of Reduced_mat"
print red_mat.shape

x201=red_mat[0:1,0:50]
x202=red_mat[0:1,50:100]
x203=red_mat[0:1,100:150]
y201=red_mat[1:2,0:50]
y202=red_mat[1:2,50:100]
y203=red_mat[1:2,100:150]

#print np.var(red_mat.transpose())

plt.scatter(x201,y201,color='red',label="Iris-setosa")
plt.scatter(x202,y202,color='green',label="Iris-versicolor")
plt.scatter(x203,y203,color='yellow',label="Iris-virginica")
plt.legend()
plt.title('Pc2 Vs Pc3')
plt.show()

