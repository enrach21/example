import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`
    
    Good Commands:
    len(), will provide length of an array
    """
    recursive=0
    
    for i in range (1, len(x)):
        print('i is equal to ' + str(i))
        j = i-1
        print('j is equal to ' + str(j))
        num_1 = x[j]
        num_2 = x[i]
        if num_1 > num_2:
            temp = num_1
            x[j] = x[i]
            x[i] = temp
            recursive = 1
            
    if recursive == 1:
        bubblesort(x)
    
    
    assert 1 == 1
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """

    assert 1 == 1
    return

