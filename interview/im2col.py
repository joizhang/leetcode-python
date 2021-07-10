"""
https://hackmd.io/@bouteille/B1Cmns09I
"""
import numpy as np


def pad2d(x, padding):
    if isinstance(padding, int):
        padding = (padding, padding, padding, padding)
    if isinstance(padding, tuple):
        if len(padding) == 2:
            padding = (padding[0], padding[0], padding[1], padding[1])
    x = np.pad(x, pad_width=((0, 0), (0, 0), (padding[0], padding[1]), (padding[2], padding[3])),
               mode='constant', constant_values=0)
    return x, padding


def _im2col_indices(x_shape, weights_shape, padding, stride):
    n, c, h, w = x_shape
    k_h, k_w, in_ch, out_ch = weights_shape
    h_out = int((h + padding[0] * 2 - (k_h - 1) - 1) / stride + 1)
    w_out = int((w + padding[0] * 2 - (k_w - 1) - 1) / stride + 1)

    # Compute matrix of index i
    # Level 1 vector.
    i0 = np.repeat(np.arange(k_h), k_w)
    # Duplicate for the other channels.
    i0 = np.tile(i0, c)
    # Create a vector with an increase by 1 at each level.
    i1 = stride * np.repeat(np.arange(h_out), w_out)
    # Create matrix of index i at every levels for each channel.
    i = i0.reshape(-1, 1) + i1.reshape(1, -1)

    # Compute matrix of index j
    # Slide 1 vector.
    j0 = np.tile(np.arange(k_w), k_h)
    # Duplicate for the other channels.
    j0 = np.tile(j0, c)
    # Create a vector with an increase by 1 at each slide.
    j1 = stride * np.tile(np.arange(w_out), h_out)
    # Create matrix of index j at every slides for each channel.
    j = j0.reshape(-1, 1) + j1.reshape(1, -1)

    k = np.repeat(np.arange(c), k_h * k_w).reshape(-1, 1)
    return k, i, j


def im2col(x, weights, padding, stride):
    n, c, h, w = x.shape
    k_h, k_w, in_ch, out_ch = weights.shape
    x, _ = pad2d(x, padding)
    k, i, j = _im2col_indices((n, c, h, w), (k_h, k_w, in_ch, out_ch), padding, stride)
    x = x[:, k, i, j]
    x = x.transpose(1, 2, 0).reshape(k_h * k_w * c, -1)
    return x


def conv2d(x, weights, bias, stride=1, padding=0):
    """

    :param x: shape is (N, C, H, W)
    :param weights: shape is (k_h, k_w, in_ch, out_ch)
    :param bias:
    :param stride:
    :param padding:
    :return:
    """
    n, c, h, w = x.shape
    k_h, k_w, in_ch, out_ch = weights.shape
    padding = (padding, padding)
    h_out = int((h + padding[0] * 2 - (k_h - 1) - 1) / stride + 1)
    w_out = int((w + padding[1] * 2 - (k_w - 1) - 1) / stride + 1)

    x_col = im2col(x, weights, padding, stride)
    weights_col = weights.transpose(3, 2, 0, 1).reshape(out_ch, -1)
    z = weights_col @ x_col
    z = z.reshape(out_ch, h_out, w_out, n).transpose(3, 0, 1, 2)
    z += bias
    return z


def main():
    batch_size = 5
    w, h, in_channels, out_channels = 5, 5, 1, 2
    kernel_size, stride, padding = 3, 1, 1
    x = np.arange(1, w * h + 1).reshape((1, 1, w, h))
    x = np.repeat(x, repeats=in_channels, axis=1)
    x = np.repeat(x, repeats=batch_size, axis=0)
    w = np.ones((kernel_size, kernel_size, in_channels, out_channels))
    b = np.zeros((batch_size, out_channels, 1, 1))
    x = conv2d(x, w, b, stride, padding)
    print(x[0, 0])


if __name__ == '__main__':
    main()
