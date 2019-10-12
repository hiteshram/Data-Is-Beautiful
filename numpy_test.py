import numpy as np

L=list(range(10))
L=np.array([3.14,4,5])
#print(np.array(L))
#print(np.random.random((3,3)))

np.random.seed(0)
x1=np.random.randint(10,size=6)
x2=np.random.randint(10,size=(3,3))
x3=np.random.randint(10,size=(3,3,3))
#print("x3 ndim: ", x3.ndim)
#print("x3 shape:", x3.shape)
#print("x3 size: ", x3.size)
#x[start:stop:step]
x1=np.array([1,2,3,4,5,6])
#print(x1)
#print(x1[1:4:1])

#z=np.concatenate([x,y])
#x=np.array([1,2,3,4])
#y=np.array([5,6,7])
#z=np.concatenate([x,y])
#print(z)

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1,x2,x3)