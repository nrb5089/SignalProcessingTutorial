# Setting up Python environment

Python should be installed on your machine under the C:\Python

# Recommended Development Environment Setup
This is my environment I use, but feel free to use whatever makes sense.

## Spyder, Pycharm, or some other IDE
	Contact IT for installation.

## No frills CMD and Notepad++
	Open up the ```Command Prompt``` using any method you like (I press the ```Windows``` key and type ```cmd``` and hit ```enter```).  
	
	Create a batch file by typing 
	
	```notepad mysetup.bat```
	
	Place the following text in the batch file (Note that you may need to adjust the paths):
	
	```
	@ECHO OFF
	DOSKEY py="<full path>\Python\python.exe"
	DOSKEY npp="<full path>\Notepad++\notepad++.exe"
	```
	
	At the time of this writing, Python should be in ```C:``` and Notepad++ should be in either ```C:\Program Files``` or ```C:\Program Files x86``` on the associated DEV machines.  Save and/or save and close the batch file.

	Type ```mysetup.bat```, this should initialize the cmd prompt to now use your short hand expressions ```py``` and ```npp``` for the respective programs.  Create a new ```.py``` file by typing 
	
	```npp hello_world.py```
	
	If ```Notepad++``` opens up with this new file, this portion works correctly.  Now add 
	
	```print('hello world!')```
	
	to your new ```.py``` file.  Save and/or save and close the new ```hello_world.py``` file.  In the CMD Prompt, type 
	
	```py hello_world.py``` 
	
	if you received a message in the next line ```hello world!```, then everything is working.  
	
	**Note**: You will have to refresh ```mysetup.bat``` for each new CMD window openned.
	
# Why Python?
Python is a relatively easy programming language that we use for signal processing demonstration and prototyping of algorithms.  The key mathematics come from operations in linear algebra and concepts in statistics/probability.  We use the analogy of 1D and 2D arrays to correspond to vectors and matrices, respectively.  The following tutorial provides some basic arithmetic and implementation syntax, along with the mathematical equivalent statements.  

# Using Numpy Arrays

NumPy is a Python library used for working with arrays. It also has functions for working in the domain of linear algebra, fourier transform, and matrices.

NumPy stands for 'Numerical Python' and comes with Python distributions such as Anaconda.


## Importing and using NumPy

Once NumPy is installed, you need to import it into your Python environment. You can do so with the following line of code:

```python
import numpy as np
```

We use `as np` so that we can refer to numpy with the shortened 'np' instead of typing out 'numpy' each time we want to use it.

## Creating a NumPy array

Vectors and Matrices are critical to understanding signal processing algorithms, we denote vectors as bold lower case $$\textbf{v}$$ and matrices as bold upper case $$\textbf{M}$$.  Tensors (informally, matrices with greater than 2 dimensions), are also represented by multidimensional arrays.

A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. 

You can create a numpy array from a Python list or tuple using the `array` function. Here's an example:

```python
import numpy as np

## Creating a 1D array (Vector)
v = np.array([1, 2, 3])
print(v)

## Creating a 2D array (Matrix)
M = np.array([[1, 2, 3], [4, 5, 6]])
print(M)

## Creating a 3D array (Tensor)
mytensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(mytensor)
```

## Array Indexing
The $$n$$th element of a vector may be denoted as $$v[n]$$ or $$v_n$$.  We will denote this in unbolded since it is scalar, i.e., $$\textbf{v} = [v_0,\dots,v_n,\dots]$$.

You can access the array elements as:

```python
import numpy as np

v = np.array([1, 2, 3, 4, 5])

print(v[1])  # Output: 2
print(v[2] + v[3])  # Output: 7
```
Likewise for matrices $$M[m,n]$$ or $$M_{m,n}$$ denotes the element in row $$m$$ and column $$n$$.
For 2D arrays, you need to use comma-separated indices:

```python
import numpy as np

M = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Accessing the element at 1st row and 2nd column
print(M[1, 2])  # Output: 8
```

## Array Slicing

NumPy arrays can be sliced, You can slice a NumPy array like this:

```python
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6, 7])

print(v[1:5])  # Output: array([2, 3, 4, 5])
```

For 2D arrays, it works similarly:

```python
import numpy as np

M = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Accessing the first 2 elements of the first 2 rows
print(M[0:2, 0:2])  # Output: array([[1, 2], [6, 7]])
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
