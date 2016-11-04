from numpy import array, dot, mean, std, empty, argsort ,size ,shape ,transpose
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt
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
			
def swithin(x,y,m1,m2):
	temp1=x-m1
	temp2=y-m2
	scatter_mat1=np.dot(temp1.transpose(),temp1)
	#print scatter_mat1.shape	
	scatter_mat2=np.dot(temp2.transpose(),temp2)
	#print scatter_mat2.shape
	scatter_mat=scatter_mat1+scatter_mat2
	return scatter_mat
	
def sbw(m1,m2,m):
	temp1=m1-m
	temp2=m2-m
	
	scatter_mat1=temp1[:, np.newaxis]*temp1
	#scatter_mat1=np.dot(temp1.transpose(),temp1)		#d*d matrix
	print "dim of scatter_mat b/w"
	print scatter_mat1.shape
	scatter_mat2=temp2[:, np.newaxis]*temp2
	print scatter_mat1.shape
	temp1=[]
	temp=[]
	scatter_mat=(56*scatter_mat1+44*scatter_mat2)
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
read_label()
data= np.array(arr,float)
arr=[]
class1=[]
class2=[]
i=0

for cell in data:
	if label[i]==-1:
		class1.append(cell)
	if label[i]==1:
		class2.append(cell)
	i=i+1

x= np.array(class1,float)			#data of class1
y= np.array(class2,float)			#data of class2

class1=[]
class2=[]

m=mean(data,0)
m1=mean(x,0)	
m2=mean(y,0)

#print m
#print m.shape
#print m1
#print m1.shape
#print m2
#print m3
sw=swithin(x,y,m1,m2)
print sw.shape
sb=sbw(m1,m2,m)
print sb.shape

s=inv(sw)*sb
print s.shape
#print s

k=1
red_mat=lda(s,data,k)

print "Dim of Reduced_mat"
print red_mat.shape


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
