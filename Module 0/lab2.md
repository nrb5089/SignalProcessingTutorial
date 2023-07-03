# Transmitter and Receivers




## In Phase & Quadrature (IQ)

In-phase Quadrature (IQ) signals are used extensively in signal processing and telecommunications. IQ representation of a signal is essential for the modulation and demodulation processes in communication systems.

To understand IQ signals, let's start with an introduction to basic concepts:

- **Baseband signal**: A signal with frequency components that are close to zero (around DC). It's the original frequency band of a signal before it's modulated for transmission.

- **Passband signal**: A signal that has been modulated to a higher frequency band for transmission. It's called a passband signal because it's within the frequency band, or "passband," of the transmission channel.

- **In-phase component (I component)**: This is the real part of a signal. 

- **Quadrature component (Q component)**: This is the imaginary part of a signal.

### Baseband IQ Representation

In the baseband IQ representation, a signal is represented by its I and Q components. The I component is the projection of the signal onto the real (or X) axis, and the Q component is the projection onto the imaginary (or Y) axis. You can think of an IQ signal as a 2D vector in this I-Q plane, with the I component representing the magnitude of the signal on the x-axis and the Q component representing the magnitude of the signal on the y-axis.

In Python, you can create an IQ signal like this:

```python
import numpy as np
import matplotlib.pyplot as plt

# Number of samples
N = 1000

# Time array
t = np.linspace(0, 2, N)

# IQ components
I = np.cos(2 * np.pi * t)
Q = np.sin(2 * np.pi * t)

# IQ signal
s = I + 1j*Q

# Plotting I, Q and IQ signal
plt.figure(0)

# Plots
plt.plot(t, I)
plt.plot(t,Q)
plt.legend(['In-Phase Component (I)','Quadrature Component (Q)'])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
```

**Important Note:**  The baseband IQ represenation is a complex value, and in practice requires two data streams (for digital) or physical ports resources (for analog).

### Passband IQ Representation

In passband representation, the baseband IQ signal is modulated to a higher frequency for transmission. This is typically achieved by mixing the baseband IQ signal with a carrier signal. The I component is mixed with a cosine wave, and the Q component is mixed with a sine wave.

The passband signal \(s(t)\) can be expressed as:

$$ s(t) = I(t)\cos(2\pi f_c t) - Q(t)\sin(2\pi f_c t) $$

where $f_c$ is the carrier frequency.

In Python, you can modulate a baseband IQ signal to a passband signal like this:

```python
# Carrier frequency
fc = 10e6

# Passband signal
s_passband = I * np.cos(2 * np.pi * fc * t) - Q * np.sin(2 * np.pi * fc * t)

# Plotting passband signal
plt.figure()
plt.plot(t, s_passband)
plt.title('Passband Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
```

In this tutorial, we saw how to represent a signal in baseband IQ form and passband form. Note that the passband representation is used for the actual transmission of the signal, and at the receiver side, the signal would be demodulated back to baseband for processing.

## Power


## Amplify or Attenuate

```python
import numpy as np

amplification_factor = np.sqrt(10)



```

## Noise Models

## Mixing

## Decimation

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
## Interpolation

## Matched Filter