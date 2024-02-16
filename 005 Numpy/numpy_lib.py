#Numpy array,usecase:->Faster Operation
import numpy as np

np_array = np.array([1, 2, 3, 4])
print(np_array)
print(type(np_array))
print(np_array.shape)

# Creating a 2d array

np_array2=np.array([(1,2,3,4),(5,6,7,8)])
print(np_array2.shape)

# Setting custom data type(here float)

np_array3=np.array([(1,2,3,4),(5,6,7,8)],dtype=float)
print(np_array2)

#creating a numpy arrays of zeros

np_zeros=np.zeros((4,5))#4 rows 5 cols set here
print(np_zeros)

#creating a numpy arrays of ones

np_ones=np.ones((4,5))#4 rows 5 cols set here
print(np_ones)

# Creating array of any particular value

np_particular=np.full((4,5),5) #array of all the values of 5
print(np_particular)

# Create of identity matrix
identity=np.eye(4)
print(identity)

# Creating a numpy array with random values(values will be within 0-1 range)
random_val=np.random.random((3,4))
print(random_val)

# rnadom intier val array with specific range
random_inti=np.random.randint(10,100,(3,4)) #3x4 matrix will be printed within range 10-100
print(random_inti)

# array of evenly spaced values->we have to mention no of values we need
space=np.linspace(10,30,7) #mentioning we need evenly spaced 6 values in range 10-30
print(space)

#array of evenly spaced values--> here we mention steps

space2=np.arange(10,30,5)
print(space2)

# Convert a list to numpy array

list2=[1,2,3,4,5,6]
arr=np.asarray(list2)
print(arr)
print(type(arr))

# Analysing a numpy array(getting various description aboutnumpy array)
test_arr=np.random.randint(10,30,(3,4))
print(test_arr)
print(test_arr.shape)
print(test_arr.ndim) #dimension of array
print(test_arr.size) # number of elements in the array
print(test_arr.dtype)#cehck data type of all the elements present in the array

# Mathematical operation in nparray

a=np.random.randint(10,20,(3,3))
b=np.random.randint(20,30,(3,3,))

print(a)
print(b)
print(a+b)
#alterbative-> print(np.add(a,b))
print(a-b)
#alterbative-> print(np.subtract(a,b))
print(a*b)
#alterbative-> print(np.multiply(a,b))
print(a/b)
#alterbative-> print(np.divide(a,b))

#Matrix manipulation
array=np.random.randint(10,20,(2,3))
print(array)
print(array.shape)

#transpose of matrix
trans=np.transpose(array)
print(trans)
print(trans.shape)
#method 2 for transpose
trans2=array.T
print(trans2)
print(trans2.shape)

# Reshaping a array
array3=np.random.random((3,2))
print(array3)
array4=array3.reshape(2,3)
print(array4)