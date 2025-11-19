import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

# # get type
print(a.dtype)

b = np.array([[2.1,6.2,8.3],[7.1, 8.2, 5.1]])
print(b.dtype)


# # get size
print(a.size)
print(a.nbytes)