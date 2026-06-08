"""Utility functions for the simplified JPEG compression notebook."""

import numpy as np


def q_tables():
    """Return three JPEG-like quantization matrices: Q10, Q50 and Q90.

    Q10 applies stronger quantization, Q50 is a standard baseline-like
    luminance matrix, and Q90 applies lighter quantization.
    """
    q50 = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99],
    ], dtype=np.float64)

    q10 = np.maximum(np.round(q50 * 2.0), 1).astype(np.float64)
    q90 = np.maximum(np.round(q50 * 0.5), 1).astype(np.float64)

    return q10, q50, q90
