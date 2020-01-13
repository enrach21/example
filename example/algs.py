import numpy as np

def insertion_sort(x):
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
    
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    
    Goal: 
    First: Select a pivot point. In this case the first bin in the list.
    Second: Put all of other items in the list ordered arround the pivot variable
    Third: Recursively do the same to each side of the list
    Fourth: If the list being sorted is 0 return it
    
    
    Variables:
    P is the pivot point
    
    """
    print('The Length is...')
    print(len(x))
    
    if len(x)==1 or len(x)==0:
        print('x is...')
        print(x)
        return x
    
    else:
        P = np.take(x, 0)
        List1 = np.array([], dtype=x.dtype)
        List2 = np.array([], dtype=x.dtype)
        for i in range (1, len(x)):
            if (x[i] < P):
                List1=np.append(List1,x[i])        
                print('List1 is...')
                print(List1)
            else:
                List2=np.append(List2,x[i])
                print('List2 is...')
                print(List2)
        return np.concatenate((quicksort(List1), P, quicksort(List2)), axis=None)
    
    
       

