import cupy as cp
import cupyx.scipy.fftpack as fft

def rceps(x, nfft=None, axis=-1):
    r"""
    Calculates the real cepstrum of an input sequence x where the cepstrum is
    defined as the inverse Fourier transform of the log magnitude DFT (spectrum)
    of a signal. It's primarily used for source/speaker separation in speech
    signal processing
    Parameters
    ----------
    x : ndarray
        Input sequence, if x is a matrix, return cepstrum in direction of axis
    nfft : int
        Size of Fourier Transform
    axis: int
        Direction for cepstrum calculation
    Returns
    -------
    ceps : ndarray
        Real/Complex cepstrum result
    """
    x = cp.asarray(x)

    ceps = fft.ifft(cp.log(cp.abs(fft.fft(x)))).real

    return ceps