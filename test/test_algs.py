import numpy as np
from example import algs

# Make arrays to be tested
Test1 = np.array([1,2,4,0,1])
Test_Empty = np.array([])
Test_Ordered = np.array([1,2,3,4,5])
Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # for now, just attempt to call the bubblesort function, should
    # actually check output
    
    # Test simple example array
    assert np.array_equal(algs.bubblesort(Test1), np.array([0,1,1,2,4]))
                          
    # Test Empty array
    assert np.array_equal(algs.bubblesort(Test_Empty), np.array([]))
    
    # Test Ordered array
    assert np.array_equal(algs.bubblesort(Test_Ordered), np.array([1,2,3,4,5]))
    
    # Test Character array
    assert np.array_equal(algs.bubblesort(Test_Char), np.array(['Dog','Snake','bird','cat','elephant']))
                          

def test_quicksort():

    # Test simple example array
    assert np.array_equal(algs.quicksort(Test1), np.array([0,1,1,2,4]))
                          
    # Test Empty array
    assert np.array_equal(algs.quicksort(Test_Empty), np.array([]))
    
    # Test Ordered array
    assert np.array_equal(algs.quicksort(Test_Ordered), np.array([1,2,3,4,5]))
    
    # Test Character array
    assert np.array_equal(algs.quicksort(Test_Char), np.array(['Dog','Snake','bird','cat','elephant']))
