# Transitioning to Signals


## Why all the emphasis on arrays?

Arrays are a fundamental part of handling and manipulating signals and images in computational and data science contexts. Both **digital** signals and images can be represented as arrays of numerical data (**analog** can only be approximated), which can then be processed and analyzed using a variety of techniques.

1. **Signals**: Signals, such as audio signals, can be represented as one-dimensional arrays. In this context, each element in the array represents the amplitude of the signal at a given point in time. The sequence of these amplitudes over time forms the audio signal. This representation allows for digital signal processing techniques to be applied, such as filtering, Fourier transformation, or any other form of signal analysis.

2. **Images**: Images can be represented as multi-dimensional arrays (typically two or three dimensions). In a grayscale image, a two-dimensional array can be used where each element represents the intensity of a pixel in the image. For color images, usually a three-dimensional array is used. The first two dimensions represent the x and y coordinates of a pixel, and the third dimension represents the red, green, and blue (RGB) color channels. Each element in this array is again a numerical value representing the intensity of the corresponding color channel at a given pixel, i.e. an 8-bit grayscale image would be a 2D array of values ranging 0-255 ($2^8-1$).

By representing signals and images as arrays, powerful mathematical and computational operations can be applied to them. This includes convolution for image filtering, Fourier transforms for frequency analysis of signals, or linear algebra operations for image transformations. It also opens the possibility for machine learning algorithms to learn from these arrays of data, which has led to advances in areas such as speech recognition, image recognition, and more.

Signal processing involves various operations such as filtering, convolution, Fourier transformation, and sampling. Here, we'll cover some basic operations using NumPy:

# Basic Signal Processing in Python/NumPy
```python
import numpy as np
```

## Generating a Simple Signal

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

## Adding Noise to the Signal

Real-world signals often come with noise. Let's add some random noise, $n\sim \mathcal{N}(\textbf{0},\sigma^2\textbf{I})$, where $n$ is a Gaussian random vector with mean $\textbf{0} = [0,\dots,0]$ and covariance matrix $\sigma^2\mathbf{I}$, where $\textbf{I}$ is the identity matrix:

```python

import numpy as np
import matplotlib.pyplot as plt

# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

# A 5 Hz waveform
a = np.cos(2 * np.pi * 5 * t)

n = np.random.normal(0, 0.5, a.shape)
a = a + n

plt.plot(t, a)
plt.show()
```

In this code, we generate random noise with the same shape as our signal, then add this noise to the original signal `a`.

![Alt text](../figs/cosine_wave_noise.png?raw=true)


# Spectral Domain vs. Time Domain and a better waveform model
Let's start with an analogy. Imagine you are listening to a symphony orchestra playing a piece of music. All the different instruments playing together create a rich, complex sound that changes over time. This is similar to a signal in the time domain.

**Time Domain:** The time domain is a representation of a signal (like the music from the orchestra) that shows how the signal changes over time. When you plot the signal in the time domain, you can see the amplitude (how loud the orchestra is playing) at each point in time. However, in this representation, it's very hard to distinguish between the sounds made by different instruments. 

Now, imagine you have a magical pair of glasses. When you put on these glasses while listening to the orchestra, instead of hearing all the sounds mixed together, you start to hear each instrument separately. The violin, the trumpet, the drums, all become individually distinguishable. This is similar to a signal in the frequency (or spectral) domain.

**Frequency (Spectral) Domain:** The frequency domain is a representation of a signal that shows the different frequencies (like the individual notes played by different instruments) that make up the overall signal. When you plot the signal in the frequency domain, you can see the amplitude (how loud each instrument is playing) for each frequency (each instrument's note). This representation is very useful when you want to analyze the signal in terms of its constituent frequencies.

In summary:

- The time domain representation of a signal shows how the signal changes over time. 
- The frequency domain representation of a signal shows the constituent frequencies of the signal.

In signal processing, we often convert signals from the time domain to the frequency domain (and vice versa) because certain types of analysis and processing are easier to perform in the frequency domain. This transformation is typically done using a mathematical technique called the Fourier transform.

## Fourier Transform

Fourier transform is a way to transform a signal from time domain to frequency domain (roughly speaking). We can use the `np.fft.fft` function to compute the one-dimensional n-point discrete Fourier Transform (DFT).  We use ```np.abs``` to compute the absolute value of each element in the array to get what is called the magnitude response of the spectrum:

```python
import numpy as np


# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

# A 5 Hz waveform
a = np.cos(2 * np.pi * 5 * t)

#Add Noise
n = np.random.normal(0, 0.5, a.shape)
a = a + n

A = np.fft.fft(a)
```

In this code, we apply the Fourier transform to our noisy signal, but how would we visualize this and identify the frequencies?  For this we must incorporate the sampling rate.  At the end of the day, were working with digital signals, therefore it is more accurate to use a waveform model 

Also... let's start using values/units closer to reality.  The RF spectrum we work with generally ranges from VHF through Ka Band (30 MHz to 40 GHz).

```python
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

fc = 100e6 #Center frequency, 100 MHz
Fs = 1e9 #Sampling frequency, 1 GHz (1 GSps)

sample_num = np.arange(500) #Index tracking sample number np.arange gives a range of values [0,1,2,...,499] (increments by 1 by default)

a = np.cos(2* np.pi * fc * sample_num/Fs)

fig,axes = plt.subplots(1,2)
axes[0].plot(sample_num[0:40]/Fs,a[0:40],marker = '.',alpha = .3)
axes[0].set_xlabel('time (seconds)')

#Add Noise
n = np.random.normal(0, 0.5, a.shape)
a = a + n

A = np.fft.fft(a)
A = np.fft.fftshift(A)
#f = np.linspace(0,Fs,len(A))
f = np.linspace(-Fs/2,Fs/2,len(A))


axes[1].plot(f/1e6,np.abs(A)) #Magnitude 
axes[1].plot(f/1e6,np.angle(A)) #Phase
axes[1].set_xlabel('frequency (MHz)')
```
![Alt text](../figs/time_freq.png?raw=true)

The key to mapping frequency from sample rate in the x-axis tick marks for the spectrum is ```f = np.linspace(-Fs/2,Fs/2,len(A))```.  Remember the FFT utilizes provides the normalized frequency spectrum between $0$ and $2\pi$, but often a centered spectrum is easier to analyze, hence we use ```A = np.fft.fftshift(A)```.  **CAUTION** do not use ```fftshift``` in combination with computations involving the FFT, it will be incorrect.



### Simulation vs. Reality

Let's take a moment to elaborate on what was generated, a cosine (or sine) wave consists of a single frequency, therefore in the frequency domain we expect a single point whose peak is proportional to the signal power.  The reason for the two lines here is that the real-valued component (in this case the signal is all-real) has a symmetry about the y-axis (a negative frequency).  This negative frequency, while purely theoretical, must be incorporated in our models for real-life applications where issues with unwanted images get included.

## Signal Filtering

Filtering is a method to remove certain ranges of frequencies. For example, we could use a simple mean filter (also known as a moving average filter) to smooth our signal, $\textbf{y} = \textbf{a} * \textbf{h}$:

```python
import numpy as np

# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

# A 5 Hz waveform
a = np.cos(2 * np.pi * 5 * t)

#Add Noise
n = np.random.normal(0, 0.5, a.shape)
a = a + n

window_size = 10
h = np.ones(window_size) / window_size

# convolve the input signal with the filter kernel
y = np.convolve(a, h, mode='same')

plt.plot(t, y)
plt.show()
```

This applies a moving average filter to our noisy signal and plots the smoothed signal.  Convolution is an operation found in various areas of, refer to [1,2] for more details on the discrete time (vector) implementation.
![Alt text](../figs/cosine_wave_noise_filtered.png?raw=true)

Remember, this is a very basic introduction. For more sophisticated signal processing tasks, you might want to look at the SciPy library, which provides more specific signal processing functionality. For complex filters, you would use convolution in the frequency domain, or use libraries such as SciPy's `signal` module, which provide ready-to-use filter design and application functions.

Generate noisy sine waves with a frequency of 200 MHz and 1200 MHz (1.2 GHz) and then apply a low-pass Butterworth filter to it with a cut-off frequency of 500 MHz.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
plt.close('all')

fft = np.fft.fft
def ffts(x): return np.fft.fftshift(fft(x))

# Generate a noisy sine wave
fc1 = 200e6 #Center frequency, 200 MHz
fc2 = 1200e6 #Center frequency, 300 MHz
Fs = 10e9 #Sampling frequency, 10 GHz (10 GSps)

sigma = 2 #Noise standard deviation


y1 = np.sin(2*np.pi * fc1 * np.arange(500)/Fs)
y2 = np.sin(2*np.pi * fc2 * np.arange(500)/Fs)

y = y1 + y2 + sigma * np.random.randn(len(y1))
Ys = ffts(y)

# Design the Butterworth filter
cutoff = 500e6
b, a = butter(4, Wn = cutoff, btype='low', fs = Fs, analog=False)

#Determine frequency response
w, h = freqz(b,a, worN = int(len(Ys)), whole = True)
H = np.fft.fftshift(h)
# H = np.hstack([np.conj(h[-1:1:-1]),h])

# Apply the filter
y_filtered = lfilter(b, a, y)
Ys_filtered = ffts(y_filtered)

f = np.linspace(-Fs/2,Fs/2,len(Ys))
fig,axes = plt.subplots(2,1,sharex = True)
axes[0].plot(f/1e6,np.abs(Ys))
axes[0].set_ylim([0,300])

axes[1].plot(f/1e6,np.abs(Ys_filtered))
axes[1].set_ylim([0,300])
axes[1].set_xlabel('frequency (MHz)')

fig1,axes1 = plt.subplots(2,1)
axes1[0].plot(f/1e6, np.abs(H))
axes1[1].plot(f/1e6, np.angle(H))
axes1[1].set_xlabel('frequency (MHz)')
plt.show()

```
![Alt text](../figs/filtered_sine.png?raw=true)

Note in the figure on the bottom that the higher frequency sine wave has been removed.  Here is a look at the frequency response of the filter to provide some more insight.  The top plot shows the magnitude response, which we see that outside our cutoff (or stopband) frequency, 500 MHz, is significantly lower.  The phase response on the bottom, while it may not appear to yield much insight at first, shows that inside the $\pm$ 500 MHz (or the passband) that the phase is "linear".  It is typical in good filter design to produce linear or near-linear phase so that the distortions accumulated while filtering are predictable, i.e. group delay.  Most signal processing texts will go into more detail, see [1,2,3].

![Alt text](../figs/butter_freq_filter_response.png?raw=true)


## Multi-Rate Signal Processing

Imagine you're at a sports game and you want to capture the most crucial moments, both as photographs and videos. 

1. **Photographs (Lower Rate):** You snap a few photos occasionally — maybe one every few minutes. This is analogous to "down-sampling" or "decimation" in multi-rate signal processing. You're capturing fewer frames over a certain period, thereby reducing the "data rate."

2. **Videos (Higher Rate):** Now, when there's a crucial play, you switch to recording a video at 60 frames per second. Here, you're capturing a lot of frames in a short amount of time. This is similar to "up-sampling" or "interpolation," where you increase the data rate.

In the world of digital signal processing, "sampling" is like taking these photos or videos. It's how we convert real-world signals (like sound or radio waves) into digital data that computers and electronics can understand.  Just like in our sports game scenario, sometimes we want to process some parts of a signal at a higher "frame rate" (or data rate) because there's more happening there. Other times, when there's less happening, we might choose a lower rate to save on data and processing power. 

**Why Do We Do Multi-Rate Signal Processing?**

1. **Efficiency:** By processing signals at rates that match their content, we can save computational resources, storage, and bandwidth.
 
2. **Flexibility:** Multi-rate processing allows us to design systems that can adapt to different situations. Think of a music streaming service that switches to a lower quality (rate) when your internet connection is weak and a higher quality when it's strong.

3. **Quality:** Sometimes, to achieve certain results (like filtering out noise or other unwanted parts of a signal), it's beneficial to first increase the rate of the signal, process it, and then bring it back down.

In Summary:

Multi-rate digital signal processing is like having a camera that can switch between taking occasional photos and shooting high-frame-rate videos, depending on what's happening. It's about adapting the "rate" of processing to best match the signal's content or the system's requirements, leading to more efficient and flexible systems. Refer to [3] for more details.

### Decimation (Downsampling)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
plt.close('all')

fft = np.fft.fft
def ffts(x): return np.fft.fftshift(fft(x))

# Generate a noisy sine wave
fc1 = 200e6 #Center frequency, 200 MHz
fc2 = 1200e6 #Center frequency, 300 MHz
Fs = 10e9 #Sampling frequency, 10 GHz (10 GSps)
ds_fac = 10 #Decimation (Downsample) factor
Fs_dec = int(Fs/10)


y1 = np.sin(2*np.pi * fc1 * np.arange(500)/Fs)
y2 = np.sin(2*np.pi * fc2 * np.arange(500)/Fs)

y = y1 + y2

# Design the Butterworth filter
cutoff = 500e6
b, a = butter(4, Wn = cutoff, btype='low', fs = Fs, analog=False)

y1_dec = y1[::ds_fac]
y_dec = y[::ds_fac]
y_filtered = lfilter(b, a, y)
y_filtered_dec = y_filtered[::ds_fac]



fig,axes = plt.subplots()
axes.plot(y1_dec)
axes.plot(y_dec)
axes.plot(y_filtered_dec)
axes.legend(['Original','Decimated','Filtered, then Decimated'])
axes.set_ylim([-3,3])
axes.set_xlabel('sample')
plt.show()
```
![Alt text](../figs/filter_decimation.png?raw=true)

### Interpolation (Upsampling*)

*More than just inserting zeros...

Imagine you are looking at a connect-the-dots puzzle, but some of the dots are missing. You can still visualize the shape or picture by drawing straight lines between the dots you can see, even if there are gaps.  Interpolation is like filling in those missing dots so that the picture is more complete and flows smoothly. Instead of having jagged straight lines, you can get a curve or a smoother line that makes more sense and provides a better idea of the whole picture.  For a simpler example, think about the temperature readings at noon over a week. If you only have readings for Monday, Wednesday, and Friday, but you want to guess (or estimate) what the temperature was on Tuesday and Thursday, you could use the readings from the days you know to make a good guess. Interpolation is the mathematical way of making that guess.  In essence, interpolation is about using what you know to estimate what you don't know. It helps in filling gaps or making smoother transitions between known points or values.

```python
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

def linear_interpolation(x,upsample_factor):
	xnew = []
	for ii in np.arange(len(x)-1):
		x_new_ii = np.linspace(x[ii],x[ii+1],upsample_factor)
		xnew.extend(x_new_ii)
	return xnew


x = [1,4,5,3,1,10]
t = np.arange(len(x))
upsample_factor = 10

xnew = linear_interpolation(x, upsample_factor)
tnew = linear_interpolation(t,upsample_factor)
fig,axes = plt.subplots()

axes.plot(tnew,xnew)
axes.plot(t,x,'.')
axes.legend(['Interpolated Signal','Original Samples'])
```


![Alt text](../figs/linear_interp_simple.png?raw=true)
References and Further Reading

[1] Alan V. Oppenheim and Ronald W. Schafer. 2009. Discrete-Time Signal Processing (3rd. ed.). Prentice Hall Press, USA.

[2] John G. Proakis and Dimitris G. Manolakis. 1996. Digital signal processing (3rd ed.): principles, algorithms, and applications. Prentice-Hall, Inc., USA.

[3] Harris, Fredric J. Multirate signal processing for communication systems. CRC Press, 2022.


# Project

## Problem 1: Efficient Filtering

```python
import numpy as np
from scipy.signal import butter, lfilter, freqz, firwin
import matplotlib.pyplot as plt
plt.close('all')
fft = np.fft.fft
ifft = np.fft.ifft

def ffts(x): return np.fft.fftshift(np.fft.fft(x))

# Generate a noisy sine wave
fc1 = 200e6 #Center frequency, 200 MHz
fc2 = 1200e6 #Center frequency, 1200 MHz
Fs = 10e9 #Sampling frequency, 10 GHz (10 GSps)

sigma = 2 #Noise standard deviation

x1 = np.sin(2*np.pi * fc1 * np.arange(500)/Fs)
x2 = np.sin(2*np.pi * fc2 * np.arange(500)/Fs)

x = x1 + x2 + sigma * np.random.randn(len(x1))

# Design the FIR filter
cutoff = 500e6
h = firwin(num_taps, cutoff / (0.5 * Fs))


#Determine convolution output length
num_zeros_pad_x = ?
num_zeros_pad_h = ?
convolution_output_length = ?
x_prefiltered = np.concatenate([x,np.zeros(num_zeros_pad_x)])
h_prefiltered = np.concatenate([h,np.zeros(num_zeros_pad_h)])

#Perform convolution via FFT
X_prefiltered = ? #FFT x
H_prefiltered = ? #FFT h
X_fft_filtered = ? #Perform the filtering
x_fft_filtered = ? #IFFT of filtered output

#Perform linear convolution
x_filtered = np.convolve(?,?,mode = 'full')



freq = np.linspace(-Fs/2,Fs/2,convolution_output_length)
fig,axes = plt.subplots(3,1,sharex = True)
axes[0].plot(freq, np.abs(ffts(x_prefiltered)))
axes[1].plot(freq, np.abs(ffts(x_filtered)))
axes[2].plot(freq, np.abs(ffts(x_fft_filtered)))
```

The expected output is 


![Alt text](../figs/fft_conv_problem_output.png?raw=true)

## Problem 2: 

## Problem 3: