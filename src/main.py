#!/usr/bin/env python3

"""main.py: Relevance Vector Machine (RVM) for regression and classification."""

__author__ = "Adrian Chiemelewski-Anders, Clara Tump, Bas Straathof \
              and Leo Zeitler"

from data import sincNoiseFree
from rvm import RVR, RVC
import numpy as np
import matplotlib.pyplot as plt


# Set a random seed
np.random.seed(0)

def initData(N, dataset):
    """Initialize the data set traning and testing examples"""
    X, T = dataset(N)

    return X, T


def main():
    N = 200
    X, T = initData(N, sincNoiseFree)

    clf = RVR()
    clf.fit(X, T, 'RBFKernel')

    print("The relevance vectors:")
    print(clf.relevanceVectors)

    # This is using training data -- should be changed of course
    TPred = np.dot(clf.muPosterior, np.transpose(clf.phi))
    plt.scatter(X,T)
    plt.scatter(X,TPred, color='r')
    plt.xlabel("x")
    plt.ylabel("t")
    plt.show()

if __name__ == '__main__':
    main()

