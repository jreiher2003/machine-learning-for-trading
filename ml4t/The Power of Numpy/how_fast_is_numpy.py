import numpy as np
import time




def how_long(func, *args):
    t0 = time.time()
    result = func(*args) # all arguments are passed in as-is
    t1 = time.time()
    return result, t1 - t0

def manual_mean(arr):
    sum = 0 
    for i in xrange(0, arr.shape[0]): # from 0 to end of number of rows
        for j in xrange(0, arr.shape[1]): # from 0 to end of number of columns
            sum = sum + arr[i,j]
    return sum / arr.size

def numpy_mean(arr):
    return arr.mean()

def test_run():
    nd1 = np.random.random((1000,10000))
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print "Manual: {:.6f} ( {:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(res_manual,t_manual,res_numpy,t_numpy)

    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"
    speedup = t_manual / t_numpy
    print "Numpy mean is ", speedup, "times faster than python manual loops."

if __name__ == "__main__":
    test_run()