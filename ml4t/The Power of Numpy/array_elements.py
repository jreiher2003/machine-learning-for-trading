import numpy as np

def test_run():
    a = np.random.rand(5,4)
    print "Array:\n", a
    print "\n"
    print "Top-left corner"
    print a[0:2, 0:2]
    print "\n"
    print "Top all rows skipping the middle column "
    print a[:, 0:3:2]

    a[0,0] = 1
    print "\nModified(replaced one elements):\n", a
    a[:, 3] = [1,2,3,4,5]
    print "\nModified(replaced a column):\n", a
    

test_run()