import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
print(a.ndim)
print(b.ndim)
print(a.shape) #.shape returns a tuple that shows the size of the array along each dimension (axis).For a 1D array, it’s just the length of the array
print(b.shape)
print(a.dtype)
print(b.dtype)
print(a.itemsize)#Your array a has integers (dtype = int64 on most 64‑bit systems).Each int64 takes 8 bytes
print(a.size)#.size gives the total number of elements in the array (regardless of dimensions).It’s basically the product of all dimensions in .shape.
print(b.size)
c=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
print(c.shape)
print(c[1,5])#c[row,coloumn],c[1,-2] will have same result i.e 13
#get a specific row
print(c[0, :])
#get a specific coloumn
print(c[:,4])
#getting a [starting index:ending index:step size]
print(c[0,1:6:2])
c[1,5]=20
print(c)
c[:,2]=[1,2]
print(c)
#3-d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
#replace
b[:,1,:]=[[9,9],[8,8]]
print(b)
print(np.zeros(2))
print(np.zeros((2,3)))
list1=[10,20,30,40]
arr1=np.array(list1)
print(arr1)
print(type(arr1))

a1=[1,2,3]
print(a1)
print(a1+a1)
a1=np.array([1,2,3])
print(a1+a1)
print(type(a1))
print(a1.shape)
b1=np.array([[1,2,3],[4,5,6]])
print(b1)
print(b1.shape)
np.zeros((2,3))
a3=np.array([5,10,15,20])
print(a3+5)
print(a3*5)
b4=np.array([[1,2,3],[4,5,6]])
print(b4.shape)
print(b4[1,1])
x = np.arange(1, 6)
y = x * 3

print(x)
print(y)
c=np.zeros((3,8))
print(c)
c1=np.ones((3,8))
print(c1)
c2=np.arange(3,20,2)
print(c2)

m=np.array([[50,56,76],[49,65,68]])
print(m)
n=np.average(m)
print(n)

high_marks_in_each_subject=np.max(m,axis=0)
print(high_marks_in_each_subject)
overall_class_average=np.average(m)
print(overall_class_average)