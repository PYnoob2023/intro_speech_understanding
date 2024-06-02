import numpy as np

def voiced_excitation(duration, F0, Fs):
    '''
    Create voiced speech excitation.
    
    @param:
    duration (scalar) - length of the excitation, in samples
    F0 (scalar) - pitch frequency, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    excitation (np.ndarray) - the excitation signal, such that
      excitation[n] = -1 if n is an integer multiple of int(np.round(Fs/F0))
      excitation[n] = 0 otherwise
    '''
    excitation = np.zeros(duration)
    period = int(np.round(Fs / F0))  # Calculate the period in samples
    for n in range(0, duration, period):
        excitation[n] = -1
    return excitation

def resonator(x, F, BW, Fs):
    '''
    Generate the output of a resonator.
    
    @param:
    x (np.ndarray(N)) - the excitation signal
    F (scalar) - resonant frequency, in Hertz
    BW (scalar) - resonant bandwidth, in Hertz
    Fs (scalar) - sampling frequency, in samples/second
    
    @returns:
    y (np.ndarray(N)) - resonant output
    '''
    N = len(x)
    y = np.zeros(N)
    
    # Calculate the resonator coefficients
    R = np.exp(-np.pi * BW / Fs)
    theta = 2 * np.pi * F / Fs
    a = [1, -2 * R * np.cos(theta), R**2]
    b = [1 - R]
    
    # Apply the resonator filter to the excitation signal
    for n in range(2, N):
        y[n] = b[0] * x[n] - a[1] * y[n-1] - a[2] * y[n-2]
    
    return y

def synthesize_vowel(duration, F0, F1, F2, F3, F4, BW1, BW2, BW3, BW4, Fs):
    '''
    Synthesize a vowel.
    
    @param:
    duration (scalar) - duration in samples
    F0 (scalar) - pitch frequency in Hertz
    F1 (scalar) - first formant frequency in Hertz
    F2 (scalar) - second formant frequency in Hertz
    F3 (scalar) - third formant frequency in Hertz
    F4 (scalar) - fourth formant frequency in Hertz
    BW1 (scalar) - first formant bandwidth in Hertz
    BW2 (scalar) - second formant bandwidth in Hertz
    BW3 (scalar) - third formant bandwidth in Hertz
    BW4 (scalar) - fourth formant bandwidth in Hertz
    Fs (scalar) - sampling frequency in samples/second
    
    @returns:
    speech (np.ndarray(samples)) - synthesized vowel
    '''
    excitation = voiced_excitation(duration, F0, Fs)
    y1 = resonator(excitation, F1, BW1, Fs)
    y2 = resonator(y1, F2, BW2, Fs)
    y3 = resonator(y2, F3, BW3, Fs)
    y4 = resonator(y3, F4, BW4, Fs)
    speech = y4
    return speech
