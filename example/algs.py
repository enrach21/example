import numpy as np
import math

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
        Assign +=1
        Condition +=1
        while x[i] < x[i-1]:
            x[i], x[i-1] = x[i-1], x[i]
            Assign +=2
            i = i-1
            Assign +=1
            Condition +=1
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


def bubbleSortRecursive(x, Complexity):
    """
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
    """
    Assign = 0
    Condition = 0
    recursive=0
    for i in range (1, len(x)):
        Assign += 1
        print('i is equal to ' + str(i))
        j = i-1
        Assign += 1
        print('j is equal to ' + str(j))
        num_1 = x[j]
        num_2 = x[i]
        Condition += 1
        if num_1 > num_2:
            temp = num_1
            x[j] = x[i]
            x[i] = temp
            recursive = 1
            
    if recursive == 1:
        bubbleSortRecursive(x, Complexity)
        
    if Complexity == True:
        return C
    else:
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
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    P is the pivot point
    
    """
    
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
    Fourth: If the list being sorted is 0 return it
    
    
    Variables:
    x is the array inputed into the function.
    Assign counts when ever an index is moved or when two elements are switched.
    Condition counts everytime two elements are compared.
    P is the pivot point
    
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
        

X = np.arange(100,1100,100)
    
# N complexity
N_Y = np.array([])
for i in X:
    N_Y = np.append(N_Y, i)

# Nlog(N) complexity 
N_logN_Y = np.array([])
for i in X:
    N_logN_Y = np.append(N_logN_Y, (i*math.log2(i)))

# N^2 complexity                         
N2Y = np.array([])
for i in X:
    N2Y = np.append(N2Y, (i*i))

Insertion_Y = np.array([])
for i in X:
    Array = np.random.rand(i)
    Insertion_Y = np.append(Insertion_Y, insertion_sort(Array)[0])
    
Bubble_Y = np.array([])
for i in X:
    Array = np.random.rand(i)
    Bubble_Y = np.append(Bubble_Y,  bubbleSort(Array)[0])
    
Quick_Y = np.array([])
for i in X:
    Array = np.random.rand(i)
    Quick_Y = np.append(Quick_Y,  quicksort_Assign(Array))


plt.plot(X, N_Y, 'o', color='blue', label='O(n)')
plt.plot(X, N2Y, 'o', color='green', label='O(n^2)')
plt.plot(X, N_logN_Y, 'o', color='red', label='O(nlog(n)')
plt.plot(X, Insertion_Y, 'o', color='black', label='Insertion Sort')
plt.plot(X, Bubble_Y, 'o', color='yellow', label='Insertion Sort')
plt.plot(X, Quick_Y, 'o', color='orange', label='Insertion Sort')
plt.show()
       

