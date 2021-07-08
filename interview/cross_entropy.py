import numpy as np
from softmax import softmax


def one_hot(labels, categories):
    N, C = labels.shape[0], categories
    y = np.zeros((N, C))
    y[np.arange(N), labels] = 1
    return y


def cross_entropy(y, y_pred):
    eps = np.finfo(float).eps
    return -np.sum(y * np.log(y_pred + eps))


if __name__ == '__main__':
    sample_m = 2
    gt = (np.random.rand(sample_m) > 0.5).astype(np.int)
    gt = one_hot(gt, categories=2)
    a = np.random.rand(sample_m, 2) * 10
    b = softmax(a, dim=1)
    loss = cross_entropy(gt, b)
    print(gt)
    print(b)
    print(loss)
