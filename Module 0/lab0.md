# Setting up Python environment

#Using Numpy Arrays

NumPy is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, fourier transform, and matrices.

NumPy stands for 'Numerical Python' and comes with Python distributions such as Anaconda.


## Importing and using NumPy

Once NumPy is installed, you need to import it into your Python environment. You can do so with the following line of code:

```python
import numpy as np
```

We use `as np` so that we can refer to numpy with the shortened 'np' instead of typing out 'numpy' each time we want to use it.

## Creating a NumPy array

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. 

You can create a numpy array from a Python list or tuple using the `array` function. Here's an example:

```python
import numpy as np

## Creating a 1D array
arr = np.array([1, 2, 3])
print(arr)

## Creating a 2D array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

## Creating a 3D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)
```

## Array Indexing

You can access the array elements just like you do with Python lists:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr[1])  # Output: 2
print(arr[2] + arr[3])  # Output: 7
```

For 2D arrays, you need to use comma-separated indices:

```python
import numpy as np

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Accessing the element at 1st row and 2nd column
print(arr_2d[1, 2])  # Output: 8
```

## Array Slicing

NumPy arrays can be sliced, similar to Python lists. You can slice a NumPy array like this:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # Output: array([2, 3, 4, 5])
```

For 2D arrays, it works similarly:

```python
import numpy as np

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Accessing the first 2 elements of the first 2 rows
print(arr_2d[0:2, 0:2])  # Output: array([[1, 2], [6, 7]])
```

## Basic Array Operations

You can perform element-wise operations on arrays like addition, subtraction, etc.

```python
import numpy as np

arr1 = np.array([1, 2, 3

])
arr2 = np.array([4, 5, 6])

## Addition
print(arr1 + arr2)  # Output: array([5, 7, 9])

## Multiplication
print(arr1 * arr2)  # Output: array([ 4, 10, 18])

## Subtraction
print(arr1 - arr2)  # Output: array([-3, -3, -3])

## Division
print(arr1 / arr2)  # Output: array([0.25, 0.4 , 0.5 ])
```

## Mathematical Functions

NumPy provides standard mathematical functions like sin, cos, exp, etc. These functions operate element-wise on an array, producing an array as output.

```python
import numpy as np

arr = np.array([0, 30, 45, 60, 90])

## Convert to radians by multiplying by pi/180
arr_radians = arr * np.pi / 180

print(np.sin(arr_radians))
```

## Statistical Functions

NumPy provides functions to calculate statistical metrics like mean, median, standard deviation, etc.

```python
import numpy as np

arr = np.array([1,2,3,4,5])

# Mean
print(np.mean(arr))  # Output: 3.0

# Median
print(np.median(arr))  # Output: 3.0

# Standard Deviation
print(np.std(arr))  # Output: 1.4142135623730951
```

Remember, this is just a basic tutorial and NumPy offers many more features and functions. For a comprehensive understanding, you should refer to the official documentation, https://numpy.org/doc/.
