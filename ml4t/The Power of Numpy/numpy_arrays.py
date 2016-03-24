import numpy as np 


def test_run():
    # list to 1 1D array
    # print np.array([2,3,4])
    # # # list to 2 2D array
    # print np.array([(2,3,4),(5,6,7)])
    # # Create Empty array
    # print np.empty(5)
    # print np.empty((5,4))
    # print np.ones((5,4))
    # print np.ones((5,4), dtype=np.int_)
    print np.zeros((9,4), dtype=np.int)
    print np.random.random((5,4))
    print np.random.rand(5,4)

def test_run2():
    np.random.seed(693)
    a = np.random.randint(0,10, size=(5,4))
    print a
    # column wise math
    print a.sum(axis=0)
    # row wise math
    print a.sum(axis=1)

    print "max columns:",a.max(axis=0)
    print "min columns:",a.min(axis=0)
    print "mean columns:", a.mean(axis=0)
    print "max rows:",a.max(axis=1)
    print "min rows:",a.min(axis=1)
    print "mean rows:", a.mean(axis=1)
    print "mean of everything:", a.mean()
    # number of rows
    print a.shape[0]
    # number of columns
    print a.shape[1]

    # number of rows x columns
    print a.size



if __name__ == "__main__":
    # test_run()
    test_run2()