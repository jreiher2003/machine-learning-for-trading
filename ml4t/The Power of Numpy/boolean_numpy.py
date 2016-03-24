import numpy as np

def test_run():
    a = np.array([(20,25,10,23,26,32,10,5,0), (0,2,50,20,0,1,28,5,0)])
    arr = np.mean(a)
    print arr
    print a
    print a > arr , "\n"

    print "all number less than the mean", a[a<arr] 
    print "\n"
    a[a<arr] = arr
    print "replace numbers less than mean with mean\n", a
    print "\n"
    print "Divide array by 2\n", a/2.0
    print "\n"
    a = np.array([(1,2,3,4,5), (10,20,30,40,50)])
    print a
    print "\n"
    b = np.array([(100,200,300,400,500), (1,2,3,4,5)])
    print b
    print "\n"
    print "Multiple array a* b\n", a * b
    print "\n"
    print "Deivide a by b\n", a/b



test_run()