import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# arr=np.array(32)
# print(arr)
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr.ndim)
# arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(arr)
# print(arr.ndim)
# arr=np.array([1,2,3,4],ndmin=5)
# print(arr)
# print(arr.ndim)
# arr=np.array([1,2,3,4])
# print(arr[0])
# print(arr[2]+arr[3])
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0,2  ])
# print(arr[1,1])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr)
# print(arr[0,0,1])
# print(arr[1,0,-1])
# arr=np.array([1,2,3,4,5,6])
# print(arr[1:4])
# print(arr[4:])
# print(arr[:4])
# print(arr[-3:-1])
# print(arr[:7:2])
# arr=np.array([1,2,3,4])
# print(arr.dtype)
# arr=np.array(["a","b","c"])
# print(arr.dtype)
# arr=np.array([1,2,3,45])
# x=arr.copy()
# arr[0]=42
# print(arr)
# print(x)
# arr=np.array([1,2,3,4])
# y=arr.view()
# arr[0]=15
# print(arr)
# print(y)
# print(x.base)
# print(y.base)
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)
# arr=np.array([1,2,3,4],ndmin=5)
# print(arr)
# print("shape of array:",arr.shape)
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(4,3)
# print(newarr)
# newarr_2d=arr.reshape(2,3,2)
# print(newarr_2d)

# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr)
# new_1=arr.reshape(4,2)
# print(new_1)
# new_1=arr.reshape(2,4)
# print(new_1)
# # new_1=arr.reshape(3,3)
# # print(new_1)

# newarr=arr.reshape(2,2,-1)
# print(newarr.ndim)
# print(newarr)
# arr=np.array([[1,2,3],[4,5,6]])
# newarr=arr.reshape(-1)
# print(newarr)
# print(newarr.ndim)

# arr=np.array([1,2,3])

# for x in arr:
#     print(x)
# arr=np.array([[[1,2,3]],[[4,5,6]]])
# for x in arr:
#     # print(x)
#     for y in x:
#         for z in y:
#             print(z)

# arr=np.array([[[1,2],[3,4],[5,6],[7,8]]])

# for x in np.nditer(arr):
#     print(x)

# arr=np.array([1,2,3])

# for x in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):
#     print(x)

# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
# for x in np.nditer(arr[:,::2]):
#     print(x)
# arr=np.array([1,2,3])
# for idx,x in np.ndenumerate(arr):
#     print(idx,x)
# arr=np.array([[[1,2,3,4],[5,6,7,8]]])
# print(arr)
# for idx,x in np.ndenumerate(arr):
#     print(idx,x)
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# arr=np.concatenate((arr1,arr2))
# print(arr)
# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# print(arr1)
# print(arr2)

# arr=np.concatenate((arr1,arr2),axis=1)
# print(arr)
# arr=np.concatenate((arr1,arr2),axis=0)
# print(arr)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)

# arr=np.hstack((arr1,arr2))
# print(arr)

# arr=np.vstack((arr1,arr2))
# print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)

# newarr=np.array_split(arr,4)
# print(newarr)
# newarr=np.array_split(arr,3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr == 4)

# print(x)

# arr = np.array([3, 2, 0, 1])

# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple'])

# print(np.sort(arr))

# arr = np.array([True, False, True])

# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])

# print(np.sort(arr))

# arr = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr[x]

# print(newarr)

# filter_arr=[]
# for element in arr:
#     if element >42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr=arr[filter_arr]

# print(filter_arr)
# print(newarr)

# arr = np.array([41, 42, 43, 44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# filter_arr = arr % 2 == 0

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

from numpy import random

x=random.randint(100)
print(x)

x=random.rand()
print(x)

x=random.randint(100,size=(5))
print(x)
x=random.randint(100,size=(3,5))
print(x)

x=random.rand(5)
print(x)

x=random.rand(3,5)
print(x)

x=random.choice([3,5,7,9])
print(x)

x=random.choice([3,5,7,9],size=(3,5))
print (x)
