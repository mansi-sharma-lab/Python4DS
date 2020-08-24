#question 1
import numpy as np

# question 2
a = np.array([1,2,3,4])
print(a)

# question 3
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)

# question 4
y = np.arange(1,18,2).reshape(3,3)
print(y)

# question 5
z = np.random.randint(0,10,(3,3))
print(z)

# question 6
m = np.array([1,2,3,4,5])
print(m)
m2 = np.reshape(m, (5,1))
print(m2)

# question 7
print(m2.shape)

# question 8
m3 = np.array([4,6,8,7,9,15,31,7,21,35])
print(m3[2],m3[3],m3[8])

# question 9
print(m3[0::2])

# question 10
m4 = np.zeros((3,3))
m4[[3,3]] = [0,0]
print(m4)