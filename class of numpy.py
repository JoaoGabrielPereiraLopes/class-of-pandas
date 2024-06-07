# import numpy and creat a array
import numpy as np
a=np.array([1,2,3])
print(a)

#creat a hash
b=np.array([(2,5,7),
            (5,3,9),
            (2,3,6)])
print(b)

# creat a hash with all objects equal 1
c=np.ones((4,3))
c[1][1]=0
print(c)

# crea a hash with the objects in diagonal equal 1
d=np.eye(10)
print(d)

#return the bigger number in b
b.max()

#return the minimus number in b
b.min()

#return sum of b
b.sum()

#return the standard deviation of b
b.std()

#return the sum of b
b.mean()