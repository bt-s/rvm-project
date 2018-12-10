#!/usr/bin/env python3

import numpy as np


def sincNoiseFree(n):
    """Generate noise-free data from the sinc function.

    Keyword arguments:
    n -- the number of of data points to be generated
    """

    X = np.linspace(-10, 10, n)
    T = np.sinc(X)
    return X, T


def sincGaussianNoise(n, sigma):
    """Generate data from the sinc function containing Gaussian noise.

    Keyword arguments:
    n -- the number of of data points to be generated
    sigma -- the noise variance
    """

    X = np.linspace(-10, 10, n)
    T = np.sinc(X) + sigma * np.random.normal(0, 1, n)
    return X, T

