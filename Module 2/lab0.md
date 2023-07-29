# Stochastic Models

Noise is ubiquitous, many problems in signal processing involve stochastic (random) elements.  When using random variables in Python (with NumPy in particular here), it is often required to 'seed' a random number generator, such that the results are reproducible.

```python
import numpy as np
np.random.seed(seed = 0)
```

This sets the random number generator for NumPy seed to `0`.

## Common Random Variables

Noise corrupts signals that we wish to measure for Detection or Estimation purposes in signal processing.  This lab provides a quick rundown of some common distributions.

### Gaussian or Normal

A Gaussian or Normal random variable is a very common type of random variable in statistics and signal processing.  We will generally model thermal heat that constitutes the noise floor in a receiver as bandlimited Gaussian noise. Its probability density function is given by the following equation:

$$f(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

where:
- $x$ is the variable
- $\mu$ is the mean or expectation of the distribution
- $\sigma$ is the standard deviation
- $\sigma^2$ is the variance

**Notation: ** I prefer to use $;$ to denote parameters rather than $|$ to denote given dependencies on other random variables, but these are generally synonymous.

We denote a Gaussian distributed random variable, $x \sim \mathcal{N}(\mu,\sigma^2)$. In Python, you can generate Gaussian random variables using the ```numpy.random.normal()``` function:

```python
import numpy as np
import matplotlib.pyplot as plt

mu = 0  # mean
sigma = 1  # standard deviation

# Generate Gaussian random variable
x = np.random.normal(mu, sigma, 10000)

# Plot histogram
plt.hist(x, bins=100, density=True)
plt.title('Histogram of Gaussian Random Variable')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Random Vectors
A random vector is simply a vector of random variables. You can think of it as a multi-dimensional generalization of a random variable.  We denote a Gaussian distributed random vector, $\textbf{x} \sim \mathcal{N}(\boldsymbol\mu,\boldsymbol\Sigma)$. A Gaussian random vector is a vector whose entries are jointly Gaussian random variables. This means that any linear combination of the entries is a Gaussian random variable. For a Gaussian random vector $\textbf{x} = [x_1, x_2, \dots, x_n]$, the probability density function (pdf) is given by:

$$f(\textbf{x}) = \frac{1}{(2\pi)^{n/2} |\boldsymbol\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\textbf{x}-\boldsymbol\mu)^T \boldsymbol\Sigma^{-1} (\textbf{x}-\boldsymbol\mu)\right)$$

Where:

- $\textbf{x}$ is the vector.
- $n$ is the dimension of the vector.
- $\boldsymbol\mu$ is the vector of means.
- $\boldsymbol\Sigma$ is the covariance matrix.
- $|\boldsymbol\Sigma|$ is the determinant of the covariance matrix.

In Python, you can generate a Gaussian random vector using the `numpy.random.multivariate_normal()` function:

```python
import numpy as np
import matplotlib.pyplot as plt

# Parameters for multivariate normal distribution
mu = [0, 0]  # mean vector
Sigma = [[1, 0], [0, 1]]  # covariance matrix

# Generate Gaussian random vector
gaussian_vector = np.random.multivariate_normal(mu, Sigma, 10000)

# Plot histogram
plt.hist2d(gaussian_vector[:,0], gaussian_vector[:,1], bins=100, cmap='hot')
plt.title('2D Gaussian Random Vector')
plt.colorbar(label='Frequency')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
```

In this example, the ```numpy.random.multivariate_normal()``` function is used to generate a 2D Gaussian random vector with specified mean vector and covariance matrix. The resulting vector is then plotted using a 2D histogram. This provides a visualization of the joint distribution of the two Gaussian random variables.

This creates a 2D Gaussian random vector with mean ```mu``` and covariance matrix . The function ```numpy.random.multivariate_normal()``` generates a 2D Gaussian random vector, and the ```.T``` transposes the result so ```x``` and ```y``` are each 1D arrays.

In the same way, you can create a N-dimensional random vector of independent and identically distributed (IID) components for any distribution by generating random variables independently.

## Leaving Kansas...

### Circularly Symmetric Complex Gaussian

Suppose we have a complex number $z = x + jy$ whose components $x\sim \mathcal{N}(\mu_x,\sigma^2/2)$ and $y\sim \mathcal{N}(\mu_y,\sigma^2/2)$, then $z$ is said to be a circularly symmetric complex Gaussian random variable denoted $z\sim\mathcal{CN}(\mu,\sigma^2)$ whose distribution is

$$f(z) = \frac{1}{\pi\sigma^2} \exp\left(-\frac{1}{\sigma^2}(z-\mu)^* (z-\mu)\right)$$

### Ricean (Rice) and Non-Central Chi-Squared degree 2

A Rician or Rice random variable, denoted $x\sim Rice(v,\sigma)$ is commonly used in wireless communications to model the distribution of signal amplitudes when there is a dominant line of sight signal along with some reflected signals.  Its probability density function is:

$$f(x; v,\sigma) = \frac{x}{\sigma^2}\exp\left(-\frac{x^2+v^2}{2\sigma^2}\right)I_0(\frac{vx}{\sigma^2})$$

where:
- $x$ is the variable
- $v$ is the noncentrality parameter
- $\sigma$ is the scale parameter
- $I_0()$ is the modified Bessel function of the first kind with order zero


A non-central chi-squared distribution is a generalization of the chi-squared distribution that is used when the observations are not exactly normally distributed. It includes a non-centrality parameter, $\lambda$, which can be used to adjust the distribution away from a pure chi-squared distribution.

The probability density function (PDF) of a non-central chi-square distribution with k degrees of freedom and non-centrality parameter λ is:

$$f(x;k,\lambda) = \frac{1}{2} \exp\left(-(x+\lambda)/2\right)\left(\frac{x}{\lambda}\right)^{k/4-1/2}I_{k-2}\left(\sqrt{\lambda x}\right)$$

where:
- $x$ is the variable
- $k$ is the number of degrees of freedom
- $\lambda$ is the non-centrality parameter
- $I_v()$ is the modified Bessel function of the first kind with order $v$

For a non-central chi-square distribution with two degrees of freedom ($k=2$), the non-central parameter $\lambda$ is equal to the square of the sum of the means of the two normally distributed random variables that are squared to create the chi-square distribution.

$$f(x;k=2,\lambda) = \frac{1}{2} \exp\left(-(x+\lambda)/2\right)I_{0}\left(\sqrt{\lambda x}\right)$$

**So What?** 

The modulus of $z\sim\mathcal{CN}(\mu,\sigma^2)$, $|z| = \sqrt{x^2 + y^2}$, is a Ricean random variable $|z|\sim Rice(|v|,\sigma/\sqrt{2})$ where $\mu_x = v\cos(\phi)$ and $\mu_y = v\sin(\phi)$.

The product of $|z|^2 = z^*z$ is a noncentral chi-squared random variable with degree 2 ($k = 2$) and noncentrality parameter $\lambda = \frac{2}{\sigma^2}(\mu_x^2 + \mu_y^2)$.  

Each distribution has its own set of trade-offs for various noisy signal measurement applications.  Check out the last chapter of [1], Chapter 15 in [3], or the chapter on detection in [2] for some examples.

Further Reading:

[1] Kay, Steven M. Fundamentals of statistical signal processing: estimation theory. Prentice-Hall, Inc., 1993.

[2] Richards, Mark A. Fundamentals of radar signal processing. McGraw-Hill Education, 2014.

[3] Scheer, Jim, and William A. Holm. "Principles of modern radar." (2010): 3-4.

# Project

## Problem 1

Plot the density function and histgram of 10000 samples using a combination of of two standard Gaussian random variables.
```python
import numpy as np
from scipy.special import i0
import matplotlib.pyplot as plt
plt.close('all')

def f(x,lam): return  1/2 * np.exp(-(x+lam)/2)*i0(np.sqrt(lam*x))

def randcn(N): return 1/np.sqrt(2) * (np.random.randn(N) + 1j * np.random.randn(N))
sigma = 2.4
mu_x = 7
mu_y = 4
lam = (mu_x**2 + mu_y**2)
# lam = (mu_x**2 + mu_y**2)
x = np.linspace(0,150,10000)
samples =  np.abs(mu_x + 1j*mu_y + np.sqrt(2) * randcn(1000000))**2

plt.figure(0)
plt.plot(x,f(x,lam))
plt.hist(samples, bins=1000, density=True)



def randcn(N): return 1/np.sqrt(2) * (np.random.randn(N) + 1j * np.random.randn(N))
sigma = 2.4
mu_x = 7
mu_y = 4
lam = (mu_x**2 + mu_y**2)
# lam = (mu_x**2 + mu_y**2)
x = np.linspace(0,150,10000)
samples1 =  sigma**2/2 * np.abs(mu_x + 1j*mu_y + randcn(1000000))**2

plt.figure(1)
plt.plot(sigma**2/2 * x,2/sigma**2 *f(2/sigma**2 *x,2/sigma**2 * lam))
plt.hist(samples1, bins=1000, density=True)
```
