import numpy as np
from scipy.io.wavfile import write

rate = 44100
LOW_FREQ = 300  # Low frequency (Hz)
HIGH_FREQ = 2000  # High frequency (Hz)
PULSE_DURATION = 0.5  # Duration for each pulse (seconds)
NUM_PULSES = 10  # Number of pulses for each frequency

# Generate a single pulse for a given frequency
def generate_pulse(freq, duration, fs):
    t = np.arange(int(fs * duration))
    return np.sin(2 * np.pi * freq * t / fs) 

# Create pulsed signal
low_pulse = generate_pulse(LOW_FREQ, PULSE_DURATION, rate)
high_pulse = generate_pulse(HIGH_FREQ, PULSE_DURATION, rate)

# Concatenate the pulses to alternate between low and high frequencies
signal = np.tile(np.concatenate([low_pulse, high_pulse]), NUM_PULSES)

scaled = np.int16(signal / np.max(np.abs(signal)) * 32767)
write('output_audio.wav', rate, scaled)



