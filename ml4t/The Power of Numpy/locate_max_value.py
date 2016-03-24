"""Locate maximum value."""

import numpy as np
import time


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    # TODO: Your code here
    return np.argmax(a)


def test_run():
    start = time.time()
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print "Array:", a
    
    # Find the maximum and its index in array
    print "Maximum value:", a.max()
    print "Index of max.:", get_max_index(a)
    endtime = time.time()
    print endtime - start


if __name__ == "__main__":
    
    test_run()
