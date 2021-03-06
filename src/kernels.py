#!/usr/local/bin/python

"""kernels.py: definition of the kernel functions used for the Relevance Vector
Machine (RVM) for regression and classification."""

__author__ = "Adrian Chiemelewski-Anders, Clara Tump, Bas Straathof \
              and Leo Zeitler"

import numpy as np
from scipy.spatial import distance
import math


def linearKernel(x, y, *args):
    """Kernel for linear separation

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (none)

    """
    return np.dot(x, y)


def linearSplineKernel(x, y, *args):
    """Univariate linear spline kernel

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (none)

    """
    return 1 \
           + x * y \
           + x * y * min(x, y) \
           - (x + y) / 2 * min(x, y) ** 2 \
           + min(x, y) ** 3 / 3


def polynomialKernel(x, y, *args):
    """Polynomial kernel for curved decision boundaries

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (int): the degree of the polynomial

    """
    return math.pow(np.dot(x, y) + 1, args[0])


def RBFKernel(x, y, *args):
    """RBF kernel that uses explicit euclidian distance between x and y,

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (float): sigma; controls the smoothness of the boundary

    """
    num = distance.euclidean(x, y)
    denom = 2 * args[0] ** 2

    return np.exp(-num / denom)


def cosineKernel(x, y, *args):
    """Cosine kernel

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (none)

    """
    return (np.pi / 4.0) * np.cos(np.pi * 0.5 * np.linalg.norm(x - y))


def logKernel(x, y, *args):
    """Logarithmic kernel

    Args:
    x (float): a datapoint
    y (float): a datapoint
    *args (none)

    """
    return np.log(1 + np.linalg.norm(x - y) ** 2)


def get_kernel(kernelName, sigma=2, p=3):
    """Gets a specific kernel

    Args:
    kernelName (str): name of the kernel that we want to obtain
    sigma (float): sigma parameter for RBFKernel
    p (int): p parameter for polynomialKernel

    """
    if kernelName == 'linearKernel':
        return linearKernel, None

    if kernelName == 'linearSplineKernel':
        return linearSplineKernel, None

    elif kernelName == 'RBFKernel':
        return RBFKernel, sigma

    elif kernelName == 'polynomialKernel':
        return polynomialKernel, p

    elif kernelName == 'cosineKernel':
        return cosineKernel, None

    elif kernelName == 'logKernel':
        return logKernel, None

