import numpy as np

def insertion_sort(x, Complexity):
    """
    Goals: 
    
    Variables:
    X is the inputted Array that wishes to be sorted
    Complexity is a boolean that is used to indicated whether the counts should be returned or the Array
    """
    C = 0
    for i in range (1, len(x)):
        C +=1
        while x[i] < x[i-1]:
            C +=1
            temp = x[i]
            x[i] = x[i-1]
            x[i-1] = temp
            i = i-1
            if i == 0:
                break
    if Complexity == True:
        return C
    else:
        return x


def bubbleSort(x, Complexity):
    """
    Goals:
    
    Variables:
    C is the complexity it goes up by one each time the array is traversed to be sorted
    as well as when two variables are compared.
    
    Good Commands:
    len(), will provide length of an array
    """
    C = 0
    n = len(x)
 
    # Traverse through all array elements
    for i in range(n):
        C += 1
        # Last i elements are already in place
        for j in range(0, n-1):
            C += 1
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if x[j] > x[j+1] :
                x[j], x[j+1] = x[j+1], x[j]
    if Complexity == True:
        return C
    else:
        return x


def bubbleSortRecursive(x, Complexity):
    """
    Goals:
    
    Variables:
    recursive is a varaible used to determine if the if statement
    in the for loop was entered. If it was then the array must be
    sorted again to ensure it is in the proper order. If it was not
    and recursive = 0 the the list is sorted.
    
    Good Commands:
    len(), will provide length of an array
    """
    C = 0
    recursive=0
    for i in range (1, len(x)):
        C += 1
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
        bubbleSortRecursive(x, Complexity)
        
    if Complexity == True:
        return C
    else:
        return x

def quicksort(x, Complexity):
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
        if Complexity == True:
            return C
        else:
            return x
    
    else:
        P = np.take(x, 0)
        Array1 = np.array([], dtype=x.dtype)
        Array2 = np.array([], dtype=x.dtype)
        for i in range (1, len(x)):
            c +=1
            if (x[i] < P):
                Array1=np.append(Array1,x[i])        
                print('List1 is...')
                print(Array1)
            else:
                Array2=np.append(Array2,x[i])
                print('List2 is...')
                print(Array2)
        if Complexity == True:
            return C + quicksort(Array1) + quicksort(Array2)
        else:
            return np.concatenate((quicksort(Array1), P, quicksort(Array2)), axis=None)
  

def complexity():
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
    X = np.arange(100,1100,100)
    Y = np.array([])
    for i in X:
        Array = np.random.rand(i)
        Y = np.append(Y, insertion_sort_complexity(Array))
    plt.plot(X, Y, 'o', color='black')
    plt.show()
       

