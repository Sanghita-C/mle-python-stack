#numpy is numeric python 
import numpy as np 
a = np.array([1,2,3])
print(a)
print(type(a))
print("shape =", a.shape)


#why numpy and not python lists or sequences ? 
'''
Looping in python is slow and becomes very inefficient when we are dealing with large datasets.
C is way more efficient that ways - however ease of use is much better for python

writing code in python is easy to read and maintain

Numpy bridges the gap between ease of use and efficiency.

Behind the scenes numpy uses C to do the heavy lifting and exposes a nice python interface to the user.

'''

#What is Vectorization ? 
'''
Vectorization is the ability to abstract explicit looping and indexing operations in code.
This is because of behind the scenes precompiled C code used by numpy.

It is way easier to read and very close to mathematical notation.

Example : c= a*b

numPy uses vectorization to perform operations on entire arrays instead of individual elements.
'''

# What is Broadcasting ?
'''
Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations.

When operating on two arrays, numpy compares their shapes element-wise.
It can implicitly expand the smaller array across the larger array so that they have compatible shapes.

And after that it performs the operation element-wise.
'''
#Numpy Array

# It is basically instance of ndarray class - which is n dimensional array object
# It can hold elements of same data type
print("**********Numpy Array Example************")
a= np .array([1,2,3,4,5,6])
print(a)
print(type(a))
print(a[2])
a[2] = 10
print(a[2])

print("slicing example - second number to 5th number", a[1:5])
print("slicing example - 0 index to 4th number",a[:4])
print("slicing example - from 4th number to end", a[3:])

b = a[1:5]
print("b = a[1:5] =", b)  

dim_arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("2D array example", dim_arr)


print("example of dim2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), dim = ",dim_arr.ndim)

#dimensions also called as axes in numpy
print("==============Analyzing Dimenion 0 Array ===================")
dim0_arr = np.array(23)
print("example of dim0 = np.array(23), dim = ",dim0_arr.ndim)
print("shape of dim0_arr = " ,dim0_arr.shape)
#shape returns a tuple of integers that specifies the number of elements along each dimension\
#For dim0, it will return an empty tuple since it has no dimensions.
print("Lenth of shape of dim0_arr = " , len(dim0_arr.shape))
#length will be 0 for dim0 array since shape is empty tuple
print("size of dim0_arr = ", dim0_arr.size)
# size returns total number of elements in the array
# for dim0 array size will be 1 since it has only one element
#print("Length of dim0_arr = ", len(dim0_arr))
# length of dim0 array will be 1 since it has one element
# difference between size and length is a) size returns total number of elements in the array. b) length returns number of elements along the first dimension (axis 0)


print("==============Analyzing Dimenion 1 Array ===================")
dim1_arr = np.array([1,2,3,4,5])
print("example of dim1 = np.array([1,2,3,4,5]), dim = ",dim1_arr.ndim)
print("shape of dim1_arr = " , dim1_arr.shape)
# shape will return (5,) since it has 5 elelments along one dimension
print("length of shape of dim1_arr = " , len(dim1_arr.shape))
# length will be 1. since the shape tuple will return one element because of one dimension
print("size of dim1_arr = " , dim1_arr.size)
# size will be 5 since it has total 5 elements
print("Length of dim1_arr = " , len(dim1_arr))
# length will be 5 since it has 5 elements along first dimension

print("==============Analyzing Dimenion 2 Array ===================")
dim2_arr = np.array([[1,2,3,4],[5,6,7,8]])
print("example of dim2 = np.array([[1,2,3,4],[5,6,7,8]]), dim = ",dim2_arr.ndim)
print("Shape of dim2_arr =", dim2_arr.shape)
# shape will return (2,4) since it has 2 rows and 4 columns
print("Length of shape of dim2_arr = " , len(dim2_arr.shape))
# length will be 2 since the tuple has two elements (2,4)
print("Size of dim2_arr = " , dim2_arr.size)
#size will be 8 since it has total 8 elements
print("Length of dim2_arr = " , len(dim2_arr))
# length will be 2 since it has 2 elements along first dimemension
# to get length along specific dimension we can use shape[index]
print("Length of dim2_arr along the 2nd dimension (columns) = ", dim2_arr.shape[1])

print("==============Analyzing Dimenion 3 Array ===================")
dim3_arr = np.array([[[1,2,3],[4,5,6]]])
print("example of dim3 = np.array([[[1,2,3],[4,5,6]]]), dim = ",dim3_arr.ndim)
print("Shape of the dim3_arr = ", dim3_arr.shape)
#shape will return (1,2,3) since it has 1 block, 2 rows and 3 columns
print("Lenghth of shape of dim3_arr =" , len(dim3_arr.shape))
# length will be 3 since the tuple has three elements (1,2,3)
print("Size of dim3_arr = " , dim3_arr.size)
# size will be 6 since it has total 6 elements
print("Length of dim3_arr =", len(dim3_arr))
# length will be 1 since it has 1 element along first dimension


print("=============Analyzing four Dimensional Array ==================" )
dim4_arr = np.array([[
                        [[1,2,3,4],
                         [5,6,7,8]],
                        [[9,10,11,12],
                         [13,14,15,16]]
                         
                    ],
                    [
                        [[1,2,3,4],
                         [5,6,7,8]],
                        [[9,10,11,12],
                         [13,14,15,16]]
                         
                    ],
                    [
                        [[1,2,3,4],
                         [5,6,7,8]],
                        [[9,10,11,12],
                         [13,14,15,16]]
                         
                    ]
                    ])         

print("dim = ", dim4_arr.ndim)
print("shape = ", dim4_arr.shape)
print("length of shape = ", len(dim4_arr.shape))
print("size = ", dim4_arr.size)
# size is always product of all elements in shape tuple
# we can picture the last two elements of shape as a matrix where last element is columns and second last is rows
print("length = ", len(dim4_arr))


print("0D arrays are called scalars")
print("1D arrays are called vectors")
print("2D arrays are called matrices")
print("3D and higher dimensions are called tensors")



#Creation of most used Numpy arrays
print("**********Creation of most used Numpy arrays************")

print("---creating array with zeroes ---")
zero_arr1d = np.zeros(5)
print("1D zero array =", zero_arr1d)
zero_arr2d = np.zeros((3,4))
print("2D zero array =\n", zero_arr2d)
zero_arr3d = np.zeros((2,3,4))
print("3D zero array =\n", zero_arr3d)

print("---creating array with ones ---")
one_arr1d = np.ones(5)
print("1D one array =", one_arr1d)
one_arr2d = np.ones((3,4))
print("2D one array =\n", one_arr2d)
one_arr3d = np.ones((2,3,4))
print("3D one array =\n", one_arr3d)

print("----creating array with np.empty() ----")
empty_arr1d = np.empty(5)
print("1D empty array =", empty_arr1d)
empty_arr2d = np.empty((3,4))
print("2D empty array =\n", empty_arr2d)

'''
note : there is difference between np.empty and np.random

np.empty creates an array without initializing its values, so it may contain arbitrary data that was already present in the allocated memory.
np.random creates an array with random values, typically uniformly distributed between 0 and 1.

so if we don't really care about the initial values and want to save time, we can use np.empty


'''

print("---creating array with np.arange() ---")
arr_range1 = np.arange(10)
print("array with np.arange(10) =", arr_range1)
#the above starts from 0 goes upto 9 withstep size of 1
arr_range2 = np.arange(5,15)
print("array with np.arange(5,15) =", arr_range2)
# the above starts from 5 goes upto 14 with step size of 1
arr_range3 = np.arange(5,20,2)
print("array with np.arange(5,20,2) =", arr_range3)
# the above starts from 5 goes upto 19 with step size of 2




#sorting in numpy
print("**********Sorting in Numpy************")
unsorted_arr = np.array([1,3,5,4,,2])
print("unsorted array =", unsorted_arr)
sorted_arr = np.sort(unsorted_arr)
print("sorted array =", sorted_arr)
#note that the original array remains unchanged
print("original unsorted array remains unchanged =", unsorted_arr)
#different types of sorting 
print("----Different types of sorting----")
arr_for_sorting = np.array([3,1,4,2,5])
print("original array =", arr_for_sorting)
print("sort in ascending order =", np.sort(arr_for_sorting))
print("sort in descendingorder = ", np.sort(arr_for_sorting)[::-1])
#here [::-1] is used to reverse the sorted array for descending order
print("sort using kind='mergesort' =", np.sort(arr_for_sorting, kind='mergesort'))
print("sort using kind='quicksort' =", np.sort(arr_for_sorting, kind='quicksort'))
print("sort using kind='heapsort' =", np.sort(arr_for_sorting, kind='heapsort'))
print("sort using kind='stable' =", np.sort(arr_for_sorting, kind='stable'))
#note that different sorting algorithms have different performance characteristics depending on the data and use case
#partition sorting 
print("----Partition Sorting----")
part_arr = np.array([7,2,1,6,8,5,3,4])
print("original array =", part_arr)
#partition around the 4th smallest element (index 3)
partitioned_arr = np.partition(part_arr,3)
print("partitioned array around 4th smallest element =", partitioned_arr)
#what partition sort does is it rearranges the array such that all elements less than the 4th smallest element come before it and all elements greater come after it
#note that the elements within the partitions are not sorted
# this is useful when we only care about finding the kth smallest/largest elements without fully sorting the array
#in this case 1,2,3 will be before 4 and 5,6,7,8 will be after it in the partitioned array
#our partitioned array will look like [2,1,3,4,8,5,7,6] or any other arrangement that satisfies the partition condition

# legsorting in numpy
print("**********Lexicographical Sorting in Numpy************")
lex_arr = np.array([[3,2],
                    [1,4],
                    [2,3],
                    [1,2]])
print("original array =\n", lex_arr)
