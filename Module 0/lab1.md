# Transitioning to Signals

## Why all the emphasis on arrays?

Arrays are a fundamental part of handling and manipulating signals and images in computational and data science contexts. Both signals and images can be represented as arrays of numerical data, which can then be processed and analyzed using a variety of techniques.

1. **Signals**: Signals, such as audio signals, can be represented as one-dimensional arrays. In this context, each element in the array represents the amplitude of the signal at a given point in time. The sequence of these amplitudes over time forms the audio signal. This representation allows for digital signal processing techniques to be applied, such as filtering, Fourier transformation, or any other form of signal analysis.

2. **Images**: Images can be represented as multi-dimensional arrays (typically two or three dimensions). In a grayscale image, a two-dimensional array can be used where each element represents the intensity of a pixel in the image. For color images, usually a three-dimensional array is used. The first two dimensions represent the x and y coordinates of a pixel, and the third dimension represents the red, green, and blue (RGB) color channels. Each element in this array is again a numerical value representing the intensity of the corresponding color channel at a given pixel, i.e. an 8-bit grayscale image would be a 2D array of values ranging 0-255 ($2^8-1$).

By representing signals and images as arrays, powerful mathematical and computational operations can be applied to them. This includes convolution for image filtering, Fourier transforms for frequency analysis of signals, or linear algebra operations for image transformations. It also opens the possibility for machine learning algorithms to learn from these arrays of data, which has led to advances in areas such as speech recognition, image recognition, and more.

Signal processing involves various operations such as filtering, convolution, Fourier transformation, and sampling. Here, we'll cover some basic operations using NumPy:

# Basic Signal Processing in Python/NumPy
```python
import numpy as np
```

## 1. Generating a Simple Signal

A simple signal could be a sine wave. To generate a sine wave:

```python
import numpy as np
import matplotlib.pyplot as plt

# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

# A 5 Hz waveform
a = np.cos(2 * np.pi * 5 * t)

plt.plot(t, a)
plt.show()
```

What's this other import ```matplotlib.pyplot```?
Matplotlib is a popular data visualization library in Python that allows users to create a wide range of high-quality plots, charts, and graphs. It provides a comprehensive set of tools for creating static, animated, and interactive visualizations.  With Matplotlib, users can generate line plots, scatter plots, bar charts, histograms, pie charts, and many other types of visual representations. It offers precise control over every aspect of a plot, including the axes, labels, colors, markers, and styles, allowing users to customize their visualizations to suit their needs.  Matplotlib is widely used in various fields such as data analysis, scientific research, engineering, finance, and more. It integrates well with other libraries and frameworks in the Python ecosystem, making it a versatile tool for data exploration and presentation.  In addition to its core functionality, Matplotlib also provides support for creating interactive plots using widgets and event handling, saving plots in different file formats, and incorporating mathematical expressions and LaTeX typesetting.

In this code, we generate a time variable `t`, and a signal `a` that is a 5Hz sine wave. Then we plot the signal using ```matplotlib```.

![Alt text](../figs/cosine_wave.png?raw=true)

## 2. Adding Noise to the Signal

Real-world signals often come with noise. Let's add some random noise to our signal:

```python
noise = np.random.normal(0, 0.5, a.shape)
a = a + noise

plt.plot(t, a)
plt.show()
```

In this code, we generate random noise with the same shape as our signal, then add this noise to the original signal `a`.



# Spectral Domain vs. Time Domain
## 3. Fourier Transform

Fourier transform is a way to transform a signal from time domain to frequency domain. We can use the `np.fft.fft` function to compute the one-dimensional n-point discrete Fourier Transform (DFT):

```python
A = np.fft.fft(a)

# Since the resulting power spectrum is symmetric, we only display the first half
A = np.abs(A[:len(A)//2])

f = np.linspace(0, 500//2, len(A), endpoint=False)

plt.plot(f, A)
plt.show()
```

In this code, we apply the Fourier transform to our noisy signal and plot the spectrum.

## 4. Signal Filtering

Filtering is a method to remove certain ranges of frequencies. For example, we could use a simple mean filter (also known as a moving average filter) to smooth our signal:

```python
window_size = 10
filter_kernel = np.ones(window_size) / window_size

# convolve the input signal with the filter kernel
a_smooth = np.convolve(a, filter_kernel, mode='same')

plt.plot(t, a_smooth)
plt.show()
```

This applies a moving average filter to our noisy signal and plots the smoothed signal.

Remember, this is a very basic introduction. For more sophisticated signal processing tasks, you might want to look at the SciPy library, which provides more specific signal processing functionality. For complex filters, you would use convolution in the frequency domain, or use libraries such as SciPy's `signal` module, which provide ready-to-use filter design and application functions.
