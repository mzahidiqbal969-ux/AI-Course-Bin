import numpy as np
#Diagonal Matrix / Extract Diagonal
x=np.diag([1,2,3])
print(x)
#extract diagonal
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b=np.diag(a)
print(b)
#np.arange(start, stop, step)
y=np.arange(0,10,2)
print(y)#Indexing, Loop replacement, Creating sequences
# np.linspace(start, stop, num)
z=np.linspace(0,1,5) #5 equally spaced values from 0 to 1 (including both 0 and 1)
print(z) #it is used in smooth data points and in plotting and predictions
print(z.shape)

idx = np.arange(0,100) #it will consider with auto 1 step
print(idx)

x1=np.diag([4,0,2])
print(x1)
