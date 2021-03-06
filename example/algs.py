import numpy as np
import math
# import matplotlib.pyplot as plt

def insertion_sort(x):
    """
    Goals: 
    The goal is to sort the an array by starting with the left most element
    and moving left to right move an element back if it is less than the previous
    element until the list is completely ordered.
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    n is the lengh of the array.
    i is the pointer to which element of the array is being looked at.
    
    Output:
    Array of...
    first is sorted array
    second is amount of conditionals called
    thris is the number of assignments
    """
    Assign = 0
    Condition = 0
    for i in range (1, len(x)): # pass through the array skipping the 0 element
        Assign +=1 # assignment of i
        Condition +=1 # while loop condition
        while x[i] < x[i-1]:
            x[i], x[i-1] = x[i-1], x[i]
            Assign +=2 # the swapping of two elements
            i = i-1
            Assign +=1 # I changing by 1
            Condition +=1 # If condition for i
            if i == 0:
                break
    return x, Assign, Condition


def bubbleSort(x):
    """
    Goals:
    The goal is to sort the array by looking at two element at a time and
    switching them if the first is less than the second and move up the array.
    Eventually after traverseing N times through the list everything will be completley
    sorted.
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched
    Condition counts everytime two elements are compared
    n is the lengh of the array
    
    Output:
    Array of...
    first is sorted array
    second is amount of conditionals called
    thris is the number of assignments
   
    """
    Assign = 0
    Condition = 0
    n = len(x)
 
    # Traverse through all array elements
    for i in range(n):
        Assign += 1
        # Last i elements are already in place
        for j in range(0, n-i-1):
            Assign += 1
            Condition += 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]
                Assign += 2
    return x, Assign, Condition


def bubbleSortRecursive(x):
    """
    I ended up not using this function
    
    Goals:
    The goal is to sort the array by looking at two element at a time and
    switching them if the first is less than the second and move up the array.
    Rather than going through the array N times however, there is a parameter
    checking to see if 
    
    Variables:
    recursive is a varaible used to determine if the if statement
    in the for loop was entered. If it was then the array must be
    sorted again to ensure it is in the proper order. If it was not
    and recursive = 0 the the list is sorted.
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    n is the lengh of the array.
    
    Output:
    An Array
    """
    Assign = 0
    Condition = 0
    recursive=0
    for i in range (1, len(x)):
        Assign += 1 # assignment of i
        j = i-1 # assignment of j
        Condition += 1 # testing to see if two elements of the list
        if x[i-1] > x[i]:
            x[i], x[i-1] = x[i-1], x[1]
            Assign += 2
            recursive = 1
    
    Condition += 1 
    if recursive == 1:
        bubbleSortRecursive(x)
    else:    
        return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    
    Goal: 
    First: Select a pivot point. In this case the first bin in the list.
    Second: Put all of other items in the list ordered arround the pivot variable
    Third: Recursively do the same to each side of the list
    Fourth: If the list being sorted is 0 or 1 return it
    
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    P is the pivot point
    
    Output:
    Sorted list
    """
    Assign = 0
    Condition=0
    
    if len(x)==1 or len(x)==0:
        Condition +=1
        return x
    
    else:
        P = np.take(x, 0)
        Assign +=1
        Array1 = np.array([], dtype=x.dtype)
        Array2 = np.array([], dtype=x.dtype)
        for i in range (1, len(x)):
            Assign +=1
            Condition +=1
            if (x[i] < P):
                Array1=np.append(Array1,x[i])
                Assign +=1
            else:
                Array2=np.append(Array2,x[i])
                Assign +=1
    return np.concatenate((quicksort(Array1), P, quicksort(Array2)), axis=None)
    
def quicksort_Assign(x):
    """
    Describe how you are sorting `x`
    
    Goal: 
    First: Select a pivot point. In this case the first bin in the list.
    Second: Put all of other items in the list ordered arround the pivot variable
    Third: Recursively do the same to each side of the list
    Fourth: If the list being sorted is 0 or 1 return it
    
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    P is the pivot point
    
    Output:
    Counts of Assign variable
    
    """
    Assign = 0
    Condition =0
    
    if len(x)==1 or len(x)==0:
        Condition +=1
        return Assign
    
    else:
        P = np.take(x, 0)
        Assign +=1
        Array1 = np.array([], dtype=x.dtype)
        Array2 = np.array([], dtype=x.dtype)
        for i in range (1, len(x)):
            Assign +=1
            Condition +=1
            if (x[i] < P):
                Array1=np.append(Array1,x[i])
                Assign +=1
            else:
                Array2=np.append(Array2,x[i])
                Assign +=1
    return quicksort_Assign(Array1) + Assign + quicksort_Assign(Array2)

def quicksort_Condition(x):
    """
    Describe how you are sorting `x`
    
    Goal: 
    First: Select a pivot point. In this case the first bin in the list.
    Second: Put all of other items in the list ordered arround the pivot variable
    Third: Recursively do the same to each side of the list
    Fourth: If the list being sorted is 0 or 1 return it
    
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    P is the pivot point
    
    Output:
    Counts of Condition variable
    
    """
    Assign = 0
    Condition =0
    
    if len(x)==1 or len(x)==0:
        Condition +=1
        return Condition
    
    else:
        P = np.take(x, 0)
        Assign +=1
        Array1 = np.array([], dtype=x.dtype)
        Array2 = np.array([], dtype=x.dtype)
        for i in range (1, len(x)):
            Assign +=1
            Condition +=1
            if (x[i] < P):
                Array1=np.append(Array1,x[i])
                Assign +=1
            else:
                Array2=np.append(Array2,x[i])
                Assign +=1
    return quicksort_Assign(Array1) + Condition + quicksort_Assign(Array2)
        
