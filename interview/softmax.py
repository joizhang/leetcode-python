import numpy as np


def softmax(x, dim=-1):
    e_x = np.exp(x - np.max(x, axis=dim, keepdims=True))
    return e_x / e_x.sum(axis=dim, keepdims=True)


if __name__ == '__main__':
    a = np.random.rand(16, 2) * 10
    b = softmax(a, dim=1)
    print(b)
