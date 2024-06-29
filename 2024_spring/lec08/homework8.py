import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
    '''
    W = np.zeros((N, N), dtype=complex)
    for k in range(N):
        for n in range(N):
            W[k, n] = np.exp(-2j * np.pi * k * n / N)
    return W
