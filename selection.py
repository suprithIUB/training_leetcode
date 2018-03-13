def partition(arr, low, high, k):
    i = low
    pivot = arr[high]
    j = high

    while i < j:
        if arr[i] > pivot:
            j-= 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i +=1

    arr[i], arr[high] = arr[high], arr[i]

    m = i - low + 1
    if m == k:
        return k
    elif m > k:
        return partition(arr, low, i-1, k)
    else:
        return partition(arr, i+1, high, k-m)

def quick_select():
    a = [2,1, 3,6,1,2,4]
    k = 4
    p = partition(a, 0, len(a)-1, len(a)-k+1)
    print(a[p])

quick_select()
