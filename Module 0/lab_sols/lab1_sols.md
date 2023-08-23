** Problem 1: Efficient Filtering **

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
h = firwin(20, cutoff / (0.5 * Fs))


#Determine convolution output length
convolution_output_length = len(h) + len(x) - 1
x_prefiltered = np.concatenate([x,np.zeros(len(h)-1)])
h_prefiltered = np.concatenate([h,np.zeros(len(x)-1)])

#Perform convolution via FFT
X_prefiltered = fft(x_prefiltered)/len(x_prefiltered)
H_prefiltered = fft(h_prefiltered)/len(h_prefiltered)
X_fft_filtered = X_prefiltered * H_prefiltered
x_fft_filtered = ifft(X_fft_filtered)

#Perform linear convolution
x_filtered = np.convolve(x,h,mode = 'full')



freq = np.linspace(-Fs/2,Fs/2,convolution_output_length)
fig,axes = plt.subplots(3,1,sharex = True)
axes[0].plot(freq, np.abs(ffts(x_prefiltered)))
axes[1].plot(freq, np.abs(ffts(x_filtered)))
axes[2].plot(freq, np.abs(ffts(x_fft_filtered)))


** Problem 2:  **

** Problem 3:  **