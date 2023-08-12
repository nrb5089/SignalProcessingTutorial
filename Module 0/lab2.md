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

We first expand to look at other types of signals used in radar and/or comms
Sure, let's dive into each of these topics.

1. **Linear Frequency Modulation (LFM) / Frequency Modulation (FM)**:
   - LFM, commonly known as a chirp in radar systems, is a signal in which the frequency changes linearly with time.
   - In an LFM signal, the instantaneous frequency increases or decreases at a constant rate over the duration of the pulse.
   - It's extensively used in radar and sonar systems, especially in pulse compression techniques, where the goal is to maintain a long pulse duration for energy purposes while achieving the range resolution of a shorter pulse through signal processing.
   - The term "chirp" comes from the similarity to the sound some birds make, which can vary in frequency.

```python
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
t = np.linspace(0,1,1000) #Time Seconds
fmin = -5 #Start Frequency Hz
fmax = 5 #Stop Frequency Hz
modulation_time = 1 #Seconds
f = np.linspace(fmin,fmax,len(t))

# Analog
lfm_signal = np.exp(1j * np.pi * (fmax-fmin)/modulation_time * t**2)

fig,ax = plt.subplots(1,2)
ax[0].plot(t,np.real(lfm_signal))
ax[0].plot(t,np.imag(lfm_signal))
ax[0].set_xlabel('Time (seconds)')


#Digital (way oversampled for visual, Nyquist would be >20 Hz)
Fs = 1000 #Sampling Rate Hz
num_samples = 40
f = np.linspace(fmin,fmax,num_samples)
lfm_signal_dig = np.exp(1j * 2*np.pi/Fs * np.cumsum(f *np.arange(num_samples)))
ax[1].plot(np.real(lfm_signal_dig),'b')
ax[1].plot(np.imag(lfm_signal_dig),'r')
ax[1].plot(np.real(lfm_signal_dig),'b.')
ax[1].plot(np.imag(lfm_signal_dig),'r.') 
```

![Alt text](../figs/lfmdemo.png?raw=true)

2. **Nonlinear Frequency Modulation (NLFM)**:
   - Unlike LFM, where the frequency changes at a constant rate, in NLFM, the rate of change of frequency is non-constant.
   - The goal of NLFM is often to achieve a constant time-bandwidth product but with a sidelobe level that is lower than what's achieved with LFM.
   - In some applications, using NLFM can reduce the peak sidelobes in the autocorrelation function, which can reduce the probability of range sidelobe false alarms in radar systems.
   - Designing and implementing NLFM waveforms can be more complex than LFM waveforms.

BPSK (Binary Phase Shift Keying) in the context of sensing or radar, especially in wireless sensor networks or remote sensing, has some unique applications and advantages. Sensing often requires sending out a known signal and examining how the environment modifies it, or it involves encoding the sensed data for transmission back to a base station.

3. **Binary Phase Shift Keying (BPSK)**:
   - BPSK is a modulation scheme where data bits modulate the phase of a reference signal (carrier wave).
   - Specifically, there are two possible phase states: 0 degrees for binary "0" and 180 degrees for binary "1" (or vice versa). The magnitude or frequency of the carrier remains unchanged.
   - BPSK is a simple and robust modulation scheme, offering good resilience against noise and interference. However, it doesn't use bandwidth as efficiently as higher order modulation schemes. This means it's slower in terms of data rate for the same bandwidth in communications.
   - Radar systems send out pulses and listen for echoes to detect and locate objects. BPSK can modulate these pulses with a binary code, enhancing detection capabilities by correlating the received signal with the known transmitted sequence.  Longer sequences lead to higher gain, see [1] for more detail.
   - BPSK-modulated radar pulses can achieve better range resolution using pulse compression techniques.
   - It's commonly used in deep space communication, digital modems, and other applications where data integrity is more crucial than bandwidth efficiency.


```python
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

t = np.linspace(0,1.3,1300)
Fs = 1000 #Sample Rate Hz
chip_rate = .1 #Seconds
samples_per_chip = int(Fs*chip_rate)

sequence = np.array([1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]) #13 Bit Barker Code

# Analog/Digital
bpsk_signal = np.repeat(sequence,samples_per_chip)

fig,ax = plt.subplots(1,2)
ax[0].plot(t,np.real(bpsk_signal))
ax[0].plot(t,np.imag(bpsk_signal))
ax[0].set_xlabel('Time (seconds)')

```
![Alt text](../figs/bpskdemo.png?raw=true)

### Passband IQ Representation

In passband representation, the baseband IQ signal is modulated to a higher frequency for transmission. Why does it need to be at a certain frequency?
Let's approach this using an analogy:

Imagine you have a variety of different-sized musical instruments: a large drum, a middle-sized guitar, and a small flute. Each of these instruments is designed to resonate or produce sound at particular frequencies. The drum produces low-pitched sounds (low frequencies), the guitar produces mid-pitched sounds (middle frequencies), and the flute produces high-pitched sounds (high frequencies). If you try to play a high-pitched song on the drum, it wouldn't sound right. Similarly, trying to get deep bass tones out of a flute would be futile. The physical design and size of each instrument make it naturally suited for specific tones or frequencies. Antennas are somewhat similar to musical instruments in this context. An antenna's size and shape determine which frequencies it can efficiently "play" or resonate with. When radio waves of a specific frequency hit an antenna, if the antenna is of the right size and design for that frequency, it resonates efficiently, turning those radio waves into electrical signals (or vice versa: turning electrical signals into radio waves). However, if you send radio waves of an unsuitable frequency to an antenna (like trying to get bass out of a flute), the antenna won't resonate well. It might still pick up the signal, but not efficiently, leading to weak reception or transmission.  So, just as you'd pick a specific musical instrument for a particular pitch or frequency range, engineers choose or design antennas for specific frequency ranges based on their applications. It ensures efficient transmission and reception of signals in communication systems.  


Reaching a higher frequency is typically achieved by mixing the baseband IQ signal with a **carrier** signal. The I component is mixed with a cosine wave, and the Q component is mixed with a sine wave.

The passband signal $s(t)$ can be expressed as:

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

**Continuous Domain (Analog Signals):**

For a continuous-time signal $x(t)$, the **power** is defined as the average power over an interval. 

For non-periodic signals, the average power $P$ over all time is given by:
$ P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 \, dt$

For periodic signals with period $T_0$, the average power $P$ is:
$P = \frac{1}{T_0} \int_{0}^{T_0} |x(t)|^2 \, dt$

Where:
- $x(t)$ is the signal.
- $T_0$ is the period of the signal.

**Discrete Domain (Digital Signals):**

For a discrete-time signal $x[n]$, the power is similarly defined. 

For non-periodic sequences, the average power $P$ over all time is:
$P = \lim_{N \to \infty} \frac{1}{2N + 1} \sum_{n=-N}^{N} |x[n]|^2$

For periodic sequences with period \( N_0 \), the average power $P$ is:
$P = \frac{1}{N_0} \sum_{n=0}^{N_0-1} |x[n]|^2$

Where:
- $x[n]$ is the signal.
- $N_0$ is the period of the sequence.

In plain English, sum of squared absolute value of elements averaged over the length of the sequence.  A scaling factor $P$ may be applied to a vector/array in order to obtain an "amplification" or "attenuation".

```python

import numpy as np
import matplotlib.pyplot as plt

# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

#Signal Power
P = 2

# A 5 Hz waveform
a = np.sqrt(P) * np.cos(2 * np.pi * 5 * t)

power_a = np.sum(np.abs(a)^2)/len(a)

```

## Notes:

1. The power of a signal represents the energy per unit of time. 

2. If a continuous or discrete signal's energy is finite, and its duration is infinite, then we speak of the signal's power rather than its energy.

3. If the power is finite for a signal that extends from $-\infty$ to $\infty$, then the signal is referred to as a power signal. If the energy is finite but the power is infinite, the signal is called an energy signal.


## Noise Models

The performance of a communication receiver is significantly impacted by noise. Noise, in a receiver, generally refers to random and unpredictable electrical signals that can degrade the quality of the received signals. This noise can originate from various sources both external and intrinsic to the receiver components.

Here are the most common types of noise in a receiver:

1. **Thermal Noise (or Johnson-Nyquist Noise):** This noise originates due to the random motion of electrons in a conductor. Its power is proportional to temperature and bandwidth. It's present in all electronic devices and components. Given by the equation:
   $ N = k \times T \times B $
   where $ k $ is Boltzmann's constant, $ T $ is the absolute temperature, and $ B $ is the bandwidth.

2. **Shot Noise:** This noise results from the discrete nature of electron charge. It's more prominent in semiconductor devices like diodes and transistors. The power of shot noise is proportional to the DC current and the bandwidth.

3. **Quantization Noise:** Relevant in digital receivers, this type of noise arises when analog signals are converted to digital. It depends on the resolution of the Analog-to-Digital Converter (ADC).

4. **Phase Noise:** Important in frequency synthesizers and oscillators, phase noise relates to the purity of the generated signals in terms of phase. It can affect the performance of systems, especially in higher order modulation schemes.

5. **Intermodulation Noise:** This type of noise arises when two or more different frequencies mix and create undesired additional frequencies, which can fall into the desired band and become a form of interference.

6. **Flicker (1/f) Noise:** This is low-frequency noise and is more prominent in some semiconductor devices at low frequencies.

7. **Environmental Noise:** This includes interference from nearby electronic devices, cosmic sources, and even solar radiation.

When designing or analyzing a receiver, engineers often consider the **Noise Figure (NF)** or **Noise Factor (F)**, which is a measure of how much the Signal-to-Noise Ratio (SNR) deteriorates as a signal passes through a component or system. A perfect component (with no noise) would have an NF of 0 dB, while real-world components always have an NF greater than 0 dB, some typical values range between 3-5 dB.

Often, in receiver design and analysis, noise is modeled as Additive White Gaussian Noise (AWGN), which assumes that noise is added to the signal and has a Gaussian distribution. This is a simplification, but it provides a reasonable model for many communication system analyses.  The python code below shows how to develop such a model based on thermal noise that is 100% in band.

```python
import numpy as np

k = 1.38e-23 #Boltzmann's Constant
T = 290 #Kelvin
NF = 10**(5/10) #Noise Factor in Linear units
B = 1e6 #Bandwidth

sigma = np.sqrt(k * T * NF * B)

```

$\sigma^2$ is the noise **variance**, and when compared to the signal power, $P$ provides the **Signal-to-Noise Ratio (SNR)**, often represented by $\chi$.  

$$ \chi = \frac{P}{\sigma^2} $$

Interference may be causing additional noise $\sigma_i^2$ from an $i$th source, the **Signal-to-Interference-plus-Noise Ratio (SINR)** is 

$$ \frac{P}{\sigma^2 + \sigma_1^2 + \dots + \sigma_i + \dots}

Note that interference models are generally much more complex.

Building from our example from lab1, if all noise is in-band, i.e. AWGN:

```python

import numpy as np
import matplotlib.pyplot as plt

# Time variable
t = np.linspace(0, 1, 500, endpoint=False)

#Signal Power
P = 1

# A 5 Hz waveform
a = np.sqrt(P) * np.cos(2 * np.pi * 5 * t)

#Noise variances
sigmas = [.1, 1, 10]

fig,ax = plt.subplots(3,1)
for ii,sigma in enumerate(sigmas):
    n = sigma * np.random.randn(len(a))
    a = a + n
    ax[ii].plot(t, a, label = f'SNR: {int(10*np.log10(P/sigma))}')
    ax[ii].legend(loc = 'lower right', fontsize = 8)

plt.show()
```

![Alt text](../figs/snrdemo.png?raw=true)



References and Further Reading

[1] Scheer, Jim, and William A. Holm. "Principles of modern radar." (2010): Chapter 20 Section 12.

