def swap(a, i, j):
    print("swap")
    print(a)
    print(i,j)
    a[i], a[j] = a[j], a[i]
    print(a)

def quick_select(a, low, high, k):
    i = low
    j = high
    pivot = a[high]

    #create a sub array from pivot -1 as ending point
    while i < j:
        if a[i] > pivot:
            j -= 1
            swap(a, i, j)
            #j -=1
            print(a)
        else:
            i += 1
    #"swap with first element that is greater than pivot")
    swap(a, i, high)
    m = i - low + 1
    print(a)
    
    print(i)    
    if m == k:
        print("match %s %s"%(m, k))
        return i
    elif m > k:
        print("m bigger than k, go left")
        return quick_select(a, low, i-1, k)
    else:
        print("pivot is too small")
        return quick_select(a, i+1, high, k-m)
    

def kth_largest(array, k):
    n = len(array)
    k = n -k+1
    print('k %s'%k)
    p = quick_select(array, 0, n-1, k)
    return array[p]

if __name__ == "__main__":
    a = [2,1, 3,6,1,2,4]
    k = 4
    print(kth_largest(a, k))
