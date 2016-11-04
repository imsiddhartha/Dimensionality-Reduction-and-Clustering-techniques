from numpy import array, dot, mean, std, empty, argsort ,size ,shape ,transpose
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
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

def swithin(x,y,z,m1,m2,m3):
	temp1=x-m1
	temp2=y-m2
	temp3=z-m3
	scatter_mat1=np.dot(temp1.transpose(),temp1)
	#print scatter_mat1.shape	
	scatter_mat2=np.dot(temp2.transpose(),temp2)
	#print scatter_mat2.shape
	scatter_mat3=np.dot(temp3.transpose(),temp3)
	#print scatter_mat3.shape	
	scatter_mat=scatter_mat1+scatter_mat2+scatter_mat3
	return scatter_mat
	
def sbw(m1,m2,m3,m):
	temp1=m1-m
	temp2=m2-m
	temp3=m3-m
	
	scatter_mat1=temp1[:, np.newaxis]*temp1
	#scatter_mat1=np.dot(temp1.transpose(),temp1)		#d*d matrix
	#print scatter_mat1
	scatter_mat2=temp2[:, np.newaxis]*temp2
	scatter_mat3=temp3[:, np.newaxis]*temp3
	scatter_mat=50*(scatter_mat1+scatter_mat2+scatter_mat3)
	#print scatter_mat.shape
	return scatter_mat

def lda(s,d,k,):
	E, V = eigh(s)				#E eigen values and V is eigen vectors	
	key = argsort(E)[::-1][:k]		#key will have indices of array
    	E, V = E[key], V[:, key]
    	V=V.transpose()
    	m = V[:,:]
    	U = np.dot(m,data.transpose())
    	#print "dim of Modified Data ",U.shape
    	return U
		
read_ip()
data= np.array(arr,float)
x=data[0:50]		#data of class1
y=data[50:100]		#data of class2
z=data[100:150]		#data of class3

m=mean(data,0)
m1=mean(x,0)	
m2=mean(y,0)
m3=mean(z,0)

#print m
#print m.shape
#print m1
#print m1.shape
#print m2
#print m3
sw=swithin(x,y,z,m1,m2,m3)
#print sw
sb=sbw(m1,m2,m3,m)
#print sb

s=inv(sw)*sb
print s.shape
print s


k=1
red_mat=lda(s,data,k)

print "Dim of Reduced_mat"
print red_mat.shape

x201=red_mat[0:1,0:50]
x202=red_mat[0:1,50:100]
x203=red_mat[0:1,100:150]
y = np.zeros((1,50))

plt.scatter(x201,y,color='red',label="Iris-setosa")
plt.scatter(x202,y,color='green',label="Iris-versicolor")
plt.scatter(x203,y,color='yellow',label="Iris-virginica")
plt.legend()
plt.title('Pc1 Vs Pc3')
plt.show()

