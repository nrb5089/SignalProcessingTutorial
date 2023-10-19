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

fig,ax = plt.subplots()
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

In Python, you can modulate a baseband IQ signal to a passband signal as shown below, note that I and Q are just placeholders and need to be defined for the code to work:

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

For periodic sequences with period $N_0$, the average power $P$ is:
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

**Notes**:

1. The power of a signal represents the energy per unit of time. 

2. If a continuous or discrete signal's energy is finite, and its duration is infinite, then we speak of the signal's power rather than its energy.

3. If the power is finite for a signal that extends from $-\infty$ to $\infty$, then the signal is referred to as a power signal. If the energy is finite but the power is infinite, the signal is called an energy signal.


## Noise Models

The performance of a communication receiver is significantly impacted by noise. Noise, in a receiver, generally refers to random and unpredictable electrical signals that can degrade the quality of the received signals. This noise can originate from various sources both external and intrinsic to the receiver components.

Here are the most common types of noise in a receiver:

1. **Thermal Noise (or Johnson-Nyquist Noise):** This noise originates due to the random motion of electrons in a conductor. Its power is proportional to temperature and bandwidth. It's present in all electronic devices and components. Given by the equation:
   $N = k \times T \times B$
   where $k$ is Boltzmann's constant, $T$ is the absolute temperature, and $B$  is the bandwidth.

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

$$ \frac{P}{\sigma^2 + \sigma_1^2 + \dots + \sigma_i + \dots} $$

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


The problems for this lab pertain to creating your own radar receiver, much more information can be found on the broad topic of radar in the MIT Lincoln Labs Introduction to Radar Course, in particular, the first lecture https://www.ll.mit.edu/sites/default/files/outreach/doc/2018-07/lecture%201.pdf.

# Problem 1
Cool, so let's build a radar receiver, but first, a little bit about Python objects/classes, we instantiate a class as 
```python
class Person:
    def __init__(self, age, name, eye_color):
        self.age = age
        self.name = name
        self.eye_color = eye_color
        
    def calculate_age_plus_five_years(self):
        return self.age + 5
```

The object class ```Person``` has accepts arguments ```name```, ```eye_color```, and ```age``` and assigns them to attributes that don't necessarily need to be name the same thing.  We instantiate an instance of ```Person``` as 

```python
bob = Person(45,'Bob', 'Brown')
```

We can do some hardcore math with the method ```calculate_age_plus_five_years``` and calclate Bob's age plus 5 years, which is 50.  
```python
bob.calculate_age_plus_five_years()
```

It's often useful to define model components as objects, for example, a Butterworth filter might use the following object wrapper

```python
from scipy.signal import butter

class ButterFilter:
	def __init__(self,N,Wn,fs,btype):
		self.N = N      #Filter order
		self.Wn = Wn    #Window limits, if low pass or high pass, it's the cutoff frequency, if bandpass, it's a tuple of start and stop
		self.Fs = fs    #Sampling Frequency
		self.btype = btype #Filter type "bandpass", "low", "high"
		
		self.b,self.a = butter(N = N, Wn = Wn, fs = fs, btype = btype)
	
	def filter_signal(self,x): return lfilter(self.b,self.a,x)
```

We instantiate ```ButterFilter``` as

```python
mybutterfilter = ButterFilter(...)
```

and filter signals by invoking the method ```mybutterfilter.filter_signal(x)```.  Your first task is to create a Python ```class``` called ```Receiver``` with attributes corresponding to:

* RF Sampling Frequency in Hz - 500 MHz
* Intermediate Frequency (IF) Sampling Frequency in Hz - 100 MHz
* Baseband (BB) Sampling Frequency in Hz - 25 MHz
* RF Center Frequency in Hz - 115 MHz
* RF Bandwidth in Hz - 10 MHz

Your class should include a function called ```__init__``` that receives args 

* ```rf_sampling_frequency_hz```
* ```if_sampling_frequency_hz```
* ```bb_sampling_frequency_hz```
* ```rf_center_frequency_hz```
* ```rf_bandwidth_hz```

and assigns them to object attributes, for example, ```self.fc_rf = rf_center_frequency_hz```.  Your ```__init__``` function should also initialize three filters 

* Butterworth front end wideband bandpass reject filter order 2 with limits 110 MHz and 120 MHz (covers the RF bandwidth)
* Chebyshev (use ```scipy.signal.cheby1```) low pass order 5 with ripple factor 2 and cutoff 20 MHz
* FIR (use ```scipy.signal.firwin```) with 31 taps and cutoff frequency of 1 MHz

Your object, ```Receiver```, should finally include a method for processing an incoming signal using components you've defined, for example

```python
def process_signal(self,wf_object,x):
    ### FOR PLOT PROCESSING ONLY ##########################
    fig,axes = plt.subplots(3,2)
    freq = np.linspace(-self.Fs_rf/2,self.Fs_rf/2,len(x))
    axes[0,0].plot(freq/1e6,affts(x))
    axes[0,0].set_xlabel('MHz')
    axes[0,1].plot(np.real(x))
    axes[0,1].plot(np.imag(x))
    #######################################################
    
    x = self.apply_bpfrontend(x) #Apply the Butterworth filter you constructed
    #Downsample by a factor of 5
    
    ### FOR PLOT PROCESSING ONLY ##########################
    freq = np.linspace(-self.Fs_if/2,self.Fs_if/2,len(x))
    axes[1,0].plot(freq/1e6,affts(x),'b')
    axes[1,0].set_xlabel('MHz')
    #######################################################
    
    # Apply the Cheby1 IF filter you constructed
    
    ### FOR PLOT PROCESSING ONLY ##########################
    axes[1,1].plot(np.real(x))
    axes[1,1].plot(np.imag(x))
    #######################################################
    
    #Downconvert to BB using a complex exponential.
    
    ### FOR PLOT PROCESSING ONLY ##########################
    axes[1,0].plot(freq/1e6,affts(x),'r')
    #######################################################
    
    #Apply the FIR BB filter
    #Downsample by a factor of 4
    
    ### FOR PLOT PROCESSING ONLY ##########################
    freq = np.linspace(-self.Fs_bb/2,self.Fs_bb/2,len(x))
    axes[2,0].plot(freq/1e6,affts(x))
    axes[2,0].set_xlabel('MHz')
    axes[2,1].plot(np.real(x))
    axes[2,1].plot(np.imag(x))
    #######################################################
    #...
return x

def ffts(x): return np.fft.fftshift(np.fft.fft(x))/len(x)
def affts(x): return np.abs(ffts(x))
```


The downsample factor causes the original signal to alias the original RF center frequency to 15 MHz,  we use a 35 MHz cutoff in the Cheby1 filter to restrict the signal at IF.  The rest of the ```process_signal``` method should apply the Cheby1 IF filter, then multiply by a complex sinusoid at  the IF, which can be calculated by 

```python
self.fc_if = np.mod(rf_sampling_frequency_hz,if_sampling_frequency_hz)
```

MHz to downconvert to baseband.  Once at baseband, apply the FIR filter you defined and downsample by a factor of 4 to reach your BB sampling frequency.  This process models the RF front end of a receiver for conversion from analog to baseband.

Write a test script to process the following LFM signal sampled at the RF receiver frequency, first instantiate an instance of your ```Receiver``` object, call it ```myreceiver``` or something that makes sense to you.

```python
pulse_width = 10e-6
Fs_rf = 500e6
fc_rf = 115e6
lfm_min = -1e6
lfm_max = 1e6
signal_length_samples = int(pulse_width * Fs_rf) #5000
x = np.exp(1j * 2 * np.pi/Fs_rf * (fc_rf *np.arange(signal_length_samples) + np.cumsum(np.linspace(lfm_min,lfm_max,signal_length_samples))))
```

The end result should look like the following:

![Alt text](../figs/rfchaintest.png?raw=true)

# Problem 2

In the first problem, you modeled the RF front end of a receiver.  Generally, the first two filter chains represent analog processes, which we try to capture functionality of in a computer simulation with discrete numbers.  A lot of times, the front end may be bypassed altogether in a model if it is not impacting to the overall setup trying to be modeled.  We now shift our focus to the signal processor, the meat of the backend that processes the raw sampled digital signal.  

Create a new Python class called ```SinglePulseWaveform``` with that has the following attributes:

* Pulse Width in seconds - 10 us
* Pulse Repetition Interval in seconds - 1000 us
* Linear Frequency Modulation Excursion in Hz- 2 MHz
* RF Sampling Frequency in Hz - 500 MHz
* Intermediate Frequency (IF) Sampling Frequency in Hz - 100 MHz
* Baseband (BB) Sampling Frequency in Hz - 25 MHz
* RF Center Frequency in Hz - 115 MHz
* RF Bandwidth in Hz - 10 MHz

and accepts the following arguments:

* pulse_width_s
* pulse_repetition_interval_s
* lfm_excursion_hz
* rf_sampling_frequency_hz 
* if_sampling_frequency_hz 
* bb_sampling_frequency_hz 
* rf_center_frequency_hz 

Assign each argument to a class attribute, similar to Problem 1.  It is of critical importance that we understand the number of samples in our timing intervals, be that a pulse width, pulse repetition interval, or in more complex cases, the coherent processing interval.  It is helpful to define a series of class attributes that precalculate these, for example, within your ```SinglePulseWaveform``` class,

```python
class SinglePulseWaveform:
    def __init__(self,
                 pulse_width_s,
                 #...
                 ):
                 self.pw = pulse_width_s
#...
    self.samples_per_pw_rf = int(self.pw * rf_sampling_frequency_hz)
    self.samples_per_pw_if = int(self.pw * if_sampling_frequency_hz)
    self.samples_per_pw_bb = int(self.pw * bb_sampling_frequency_hz)
```

The above snippet has precalculations for the number of samples in a pulse at the various sampling rates we use in our receiver.  Add these for the pulse width and pulse repetition interval.  Add a third set of attributes for the number of samples in the receiving window, more on this later, but for now use the snippet below.  Additionally, for single pulse modes, we are only interested in a critical processing interval (CPI) of one pulse.

```python
    self.samples_per_range_window_rf = self.samples_per_pri_rf - self.samples_per_pw_rf
    self.samples_per_range_window_if = self.samples_per_pri_if - self.samples_per_pw_if
    self.samples_per_range_window_bb = self.samples_per_pri_bb - self.samples_per_pw_bb
    
    self.samples_per_cpi_rf = int(1 * self.samples_per_pri_rf)
    self.samples_per_cpi_if = int(1 * self.samples_per_pri_if)
    self.samples_per_cpi_bb = int(1 * self.samples_per_pri_bb)
```

Create an array representing the LFM pulse signal described by the class attributes in ```SinglePulseWaveform```, note the sampling frequency is at RF.

```python
self.wf_single_pw = np.exp(1j * 2 * np.pi/self.Fs_rf * (self.fc_rf *np.arange(self.samples_per_pw_rf) + np.cumsum(np.linspace(self.fmin_bb,self.fmax_bb,self.samples_per_pw_rf))))
```

Concatenate ```self.wf_single_pw``` with zeros (use ```np.concantenate``` and ```np.zeros```) to form an array that represents one PRI.  The number of zeros should be specified by ```self.samples_per_range_window_rf```.  When specifying the array of zeros, it's often good practice to add ```0j``` to complexify it.  Sometimes Python will only preserve the real portion otherwise.  Name the final attribute of concatenated ```self.wf_single_pw``` and zeros as ```self.wf```

Finally, add attributes for the matched filter taps at BB, I also like to add an attribute that's a custom BB FIR (similar to what you constructed in Problem 1) custom to the waveform I'm describing so that I don't mess things up later.

```python
self.mf_wf_bb = np.exp(1j * 2 * np.pi/self.Fs_bb * (np.cumsum(np.linspace(-lfm_excursion_hz/2,lfm_excursion_hz/2,self.samples_per_pw_bb))))
self.bb_filter = FIR(numtaps = 31, cutoff = lfm_excursion_hz/2, fs = self.Fs_bb)
```

Create an instance of ```SinglePulseWaveform``` called ```mywf``` with the argument values listed above as an attribute to your ```Receiver``` object in Problem 1.  Use the function ```process_signal``` on ```mywf.wf_single_pw``` that you constructed in Problem 1 for the RF frontend.  Apply your the matched filter by appending the following at the end of the  ```process_signal``` function

```python
x = np.convolve(x,np.conj(self.mywf.mf_wf_bb), mode = 'same')
```

The output should look like 

![Alt text](../figs/mftest.png?raw=true)

# Problem 3

![Alt text](../figs/radar_return.png?raw=true)

(graphic from https://www.researchgate.net/figure/Radar-signal-concept_fig1_276184180)

All radar detection is based on delays relative to intervals in which measurements are processed.  In this problem, you'll be shown how to simulate a delay within that interval.  Let's say we have a target out at 50 km, with our chosen $T_{\textnormal{PRI}} = 1000$ us we can detect a target, unambiguously, out to 

$$R_\textnormal{ua} = cT_{\textnormal{PRI}}/2 = 150 \textnormal{km}$$

where $c = 3\times 10^8$ m/s is the speed of light in free space.  We can simulate the return signal within our receive window as 

```python
    #Calculate index of signal presence
    d = 50000 #distance of target in meters
    distance_samples_skin_return_m = np.arange(myreceiver.mywf.samples_per_cpi_rf) / myreceiver.Fs_rf * 3e8/2
    print(f'Maximum Distance: {np.max(distance_samples_skin_return_m)}, Target Distance: {d}')
    min_range_sample_to_d = np.argmin(np.abs(distance_samples_skin_return_m-d))

    #Truncate return signals outside cpi, and concatenate zeros
    x = dcp(myreceiver.mywf.wf)
    fig,axes = plt.subplots()

    x = x[:(myreceiver.mywf.samples_per_cpi_rf-min_range_sample_to_d)]
    x = np.concatenate([np.zeros(myreceiver.mywf.samples_per_cpi_rf-len(x)) + 0.0j,x])
```

Process ```x``` in the above snippet using your ```process_signal``` function constructed in Problem 1, then apply your matched filter from the ```SinglePulseWaveform``` instance you created, ```mywf```.  The output should look like the following, note the delay is roughly a third of the way through the overall receive window samples.  Matching this sample to a moment in time, then scaling by $c/2$ provides the distance estimation of the target.  But how do designate something as a detection, or not?  Surely noise can trigger detections if significant enough, let's find out in the next lab...

![Alt text](../figs/distance_delay_test.png?raw=true)