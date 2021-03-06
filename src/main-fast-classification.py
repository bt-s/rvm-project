#!/usr/bin/env python2

"""main-fast-classification.py: Testing fast RVC on a toy classification data set."""

__author__ = "Adrian Chiemelewski-Anders, Clara Tump, Bas Straathof \
              and Leo Zeitler"

from data import createSimpleClassData
from rvm import RVC
import numpy as np
import matplotlib.pyplot as plt

# Set a random seed
np.random.seed(0)


def main():
    N = 200
    w = np.array([1, 1])
    Xtrain, Ttrain = createSimpleClassData(N, w)
    Xtest, Ttest = createSimpleClassData(int(N / 3), w)

    # Set the convergence threshold to a comparably big value when using
    # linear kernel due to the fast convergence
    clf = RVC(Xtrain,
              Ttrain,
              'linearKernel',
              beta=0.001**-2,
              alphaThresh=10e8,
              convergenceThresh=10e-2,
              useFast=True)
    clf.fit()

    print("The relevance vectors:")
    print(clf.relevanceVectors)

    TPred = clf.predict(Xtest)

    correct_classifications = Xtest.dot(w) > 0
    pos_data = Xtest[correct_classifications == True]
    neg_data = Xtest[correct_classifications == False]

    plt.figure()
    plt.scatter(pos_data[:, 0], pos_data[:, 1], label='Positive Data')
    plt.scatter(neg_data[:, 0], neg_data[:, 1], label='Negative Data')

    plt.xlabel("x")
    plt.ylabel("t")
    plt.legend()
    plt.show()

    plt.figure()

    prediction_classification = TPred > 0.5
    pos_data = Xtest[prediction_classification == True]
    neg_data = Xtest[prediction_classification == False]

    pos_sigmas = TPred[prediction_classification == True]
    neg_sigmas = TPred[prediction_classification == False]

    plt.scatter(pos_data[:, 0],
                pos_data[:, 1],
                s=pos_sigmas ** 2 * 50,
                label='Positive Data')
    plt.scatter(neg_data[:, 0],
                neg_data[:, 1],
                s=(1-neg_sigmas) ** 2 *50,
                label='Negative Data')

    plt.xlabel("foobar")
    plt.ylabel("t")
    plt.legend()
    plt.show()

    print(correct_classifications)
    print(prediction_classification)

    print('accuracy',
          (correct_classifications == prediction_classification).sum() \
          / correct_classifications.shape[0])

    print('alpha shape', clf.alpha.shape)
    print(clf.alpha)

if __name__ == '__main__':
    main()

