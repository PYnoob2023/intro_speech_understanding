import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    
    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples
    
    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames
    '''
    num_frames = 1 + (len(waveform) - frame_length) // step
    frames = np.zeros((frame_length, num_frames))
    for t in range(num_frames):
        frames[:, t] = waveform[t * step : t * step + frame_length]
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    
    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)
    
    @returns:
    stft (np.ndarray((frame_length,num_frames))) - the STFT (complex-valued)
    '''
    stft = np.fft.fft(frames, axis=0)
    return stft

def stft_to_spectrogram(stft):
    '''
    Calculate the level, in decibels, of each complex-valued sample of the STFT,
    normalized so the highest value is 0dB, 
    and clipped so that the lowest value is -60dB.
    
    @params:
    stft (np.ndarray((frame_length,num_frames))) - STFT (complex-valued)
    
    @returns:
    spectrogram (np.ndarray((frame_length,num_frames)) - spectrogram (real-valued)
    '''
    spectrogram = 20 * np.log10(np.abs(stft))
    spectrogram -= np.amax(spectrogram)
    spectrogram = np.clip(spectrogram, -60, 0)
    return spectrogram
