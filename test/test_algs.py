import numpy as np
from example import algs

# Make arrays to be tested
Test1 = np.array([1,2,4,0,1])
Test_Empty = np.array([])
Test_Ordered = np.array([1,2,3,4,5,6,7,8])
Test_Reversed = np.array([8,7,6,5,4,3,2,1])
Test_Char = np.array(['cat','Dog','elephant','Snake','bird'])


def test_intertion_sort():

    # Test the complexity and accuracy of intertion sort
    assert np.array_equal(insertion_sort(Test_Ordered, Complexity=FALSE), np.array([1,2,3,4,5,6,7,8]))


def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # for now, just attempt to call the bubblesort function, should
    # actually check output
    
    # Test the complexity and accuracy of intertion sort for an ordered array
    assert np.array_equal(algs.bubbleSort(Test_Ordered, Complexity=False), np.array([1,2,3,4,5,6,7,8]))
    assert algs.bubbleSort(Test_Ordered, Complexity=True) == 64
    
    # Test the complexity and accuracy of intertion sort for an reversed array
    assert np.array_equal(algs.bubbleSort(Test_Reversed, Complexity=False), np.array([1,2,3,4,5,6,7,8]))
    assert algs.bubbleSort(Test_Reversed, Complexity=True) == 64
    
    # Test simple example array
    assert np.array_equal(algs.bubbleSort(Test1, Complexity=False), np.array([0,1,1,2,4]))
                          
    # Test Empty array
    assert np.array_equal(algs.bubbleSort(Test_Empty, Complexity=False), np.array([]))
    
    # Test Ordered array
    assert np.array_equal(algs.bubbleSort(Test_Ordered, Complexity=False), np.array([1,2,3,4,5]))
    
    # Test Character array
    assert np.array_equal(algs.bubbleSort(Test_Char, Complexity=False), np.array(['Dog','Snake','bird','cat','elephant']))
                          

def test_quicksort():

    # Test simple example array
    assert np.array_equal(algs.quicksort(Test1, Complexity=False), np.array([0,1,1,2,4]))
                          
    # Test Empty array
    assert np.array_equal(algs.quicksort(Test_Empty, Complexity=False), np.array([]))
    
    # Test Ordered array
    assert np.array_equal(algs.quicksort(Test_Ordered, Complexity=False), np.array([1,2,3,4,5]))
    
    # Test Character array
    assert np.array_equal(algs.quicksort(Test_Char, Complexity=False), np.array(['Dog','Snake','bird','cat','elephant']))
