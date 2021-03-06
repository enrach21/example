import numpy as np
import math
from example import algs

# Make arrays to be tested
Test1 = np.array([1,2,4,0,1])
Test_Empty = np.array([])
Test_Ordered = np.array([1,2,3,4,5,6,7,8])
Test_Reversed = np.array([8,7,6,5,4,3,2,1])
Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])


def test_intertion_sort():
    TestOdd = np.array([1,2,4,0,1])
    Test_Empty = np.array([])
    Test_Ordered = np.array([1,2,3,4,5,6,7,8])
    Test_Reversed = np.array([8,7,6,5,4,3,2,1])
    Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])
    
    # Empty
    assert np.array_equal(algs.insertion_sort(Test_Empty)[0], np.array([]))
    
    # Odd 
    assert np.array_equal(algs.insertion_sort(TestOdd)[0], np.array([0,1,1,2,4]))
    
    # Ordered array
    assert np.array_equal(algs.insertion_sort(Test_Ordered)[0], np.array([1,2,3,4,5,6,7,8]))
    
    # Reversed array
    assert np.array_equal(algs.insertion_sort(Test_Reversed)[0], np.array([1,2,3,4,5,6,7,8]))
    
    # Character
    assert np.array_equal(algs.insertion_sort(Test_Char)[0], np.array(['Dog','Snake','bird','cat','elephant']))


def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # for now, just attempt to call the bubblesort function, should
    # actually check output
    TestOdd = np.array([1,2,4,0,1])
    Test_Empty = np.array([])
    Test_Ordered = np.array([1,2,3,4,5,6,7,8])
    Test_Reversed = np.array([8,7,6,5,4,3,2,1])
    Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])
 
    # Empty
    assert np.array_equal(algs.bubbleSort(Test_Empty)[0], np.array([]))
    
    # Odd 
    assert np.array_equal(algs.bubbleSort(TestOdd)[0], np.array([0,1,1,2,4]))
    
    # Ordered array
    assert np.array_equal(algs.bubbleSort(Test_Ordered)[0], np.array([1,2,3,4,5,6,7,8]))
    
    # Reversed array
    assert np.array_equal(algs.bubbleSort(Test_Reversed)[0], np.array([1,2,3,4,5,6,7,8]))
    
    # Character
    assert np.array_equal(algs.bubbleSort(Test_Char)[0], np.array(['Dog','Snake','bird','cat','elephant']))
    
    # Run function on range of length
    X = np.arange(100,1100,100)
    for i in X:
        Array = np.random.rand(i)
        algs.bubbleSort(Array)[0]
                          

def test_quicksort():
    TestOdd = np.array([1,2,4,0,1])
    Test_Empty = np.array([])
    Test_Ordered = np.array([1,2,3,4,5,6,7,8])
    Test_Reversed = np.array([8,7,6,5,4,3,2,1])
    Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])
    
    # Empty
    assert np.array_equal(algs.quicksort(Test_Empty), np.array([]))
    
    # Odd 
    assert np.array_equal(algs.quicksort(TestOdd), np.array([0,1,1,2,4]))
    
    # Ordered array
    assert np.array_equal(algs.quicksort(Test_Ordered), np.array([1,2,3,4,5,6,7,8]))
    
    # Reversed array
    assert np.array_equal(algs.quicksort(Test_Reversed), np.array([1,2,3,4,5,6,7,8]))
    
    # Character
    assert np.array_equal(algs.quicksort(Test_Char), np.array(['Dog','Snake','bird','cat','elephant']))
    
        # Run function on range of length
    X = np.arange(100,1100,100)
    for i in X:
        Array = np.random.rand(i)
        algs.quicksort(Array)[0]
        

