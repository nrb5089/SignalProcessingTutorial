**Problem 1: Matrix Operations**

Given two matrices `A` and `B`:

`A = np.array([[1, 2], [3, 4], [5, 6]])` 

`B = np.array([[2, 5, 11], [7, 10,3]])` 

Write a Python script to perform the following operations using `@`, `.T`, and `*`:

1. Matrix Multiplication of A and B
2. Element-wise Multiplication of A's transpose and B

**Solution 1:**

```python
import numpy as np

# Define the matrices
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2, 5, 11], [7, 10,3]])

# Matrix multiplication
AB = A@B
print("Matrix multiplication of A and B:\n", AB)

# Element-wise multiplication
elementwise = np.multiply(A.T, B)
print("Element-wise multiplication of A's transpose and B:\n", elementwise)
```

**Problem 2: Determinant and Inverse**

Given a matrix `C = np.array([[4, 7, 9, 12], [2, 6, 1, 0.5], [1, 10, 1, 4], [5, 4, 6, 1]])`, calculate:

1. The determinant of C
2. The inverse of C

**Solution 2:**

```python
import numpy as np

# Define the matrix
C = np.array([[4, 7, 9, 12], [2, 6, 1, 0.5], [1, 10, 1, 4], [5, 4, 6, 1]])

# Determinant
det_C = np.linalg.det(C)
print("Determinant of C:\n", det_C)

# Inverse
inv_C = np.linalg.inv(C)
print("Inverse of C:\n", inv_C)
```

**Problem 3: Eigenvalues and Eigenvectors**

For the same matrix `C`, compute:

1. The eigenvalues of C
2. The eigenvectors of C

**Solution 3:**

```python
import numpy as np

# Define the matrix
C = np.array([[4, 7, 9, 12], [2, 6, 1, 0.5], [1, 10, 1, 4], [5, 4, 6, 1]])

# Eigenvalues and eigenvectors
d, V = np.linalg.eig(C)
print("Eigenvalues of C:\n", d)
print("Eigenvectors of C:\n", V)

D = np.diag(d)

Cr = V@D@np.linalg.inv(V)
print("Reconstructed C:\n", Cr)

#The complex component can be removed by
print("Clean Reconstructed C:\n", np.real(Cr))

```

