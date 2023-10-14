import numpy as np
from scipy.io.wavfile import write, read
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

rate = 44100
LOW_FREQ = 300  # Low frequency (Hz)
HIGH_FREQ = 2000  # High frequency (Hz)
PULSE_DURATION = 0.5  # Duration for each pulse (seconds)
NUM_PULSES = 10  # Number of pulses for each frequency
signal = read('output_audio.wav')[1]/32767.0

# Design the LPF
cutoff = 500
b, a = butter(4, Wn = cutoff, btype='low', fs = rate, analog=False)

new_signal = lfilter(b, a, signal) 
scaled = np.int16(new_signal / np.max(np.abs(new_signal)) * 32767)
#new_signal = filter_signal(signal) 


write('filtered_out_high_audio.wav', rate, scaled)



