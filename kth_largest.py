def partition(array, low, high):
    from random import randint
    pivot_index = randint(low, high)
    pivot = array[high]
    smaller = low -1
    for i in range(low, high): # high -1 because of range behavior
        if array[i] <= pivot:
            smaller +=1
            array[smaller], array[i] = array[i], array[smaller]
    array[smaller+1], array[high] = pivot, array[smaller+1]
    return smaller+1

def quick_sort(array, low, high):
    if low <= high:
        part = partition(array, low, high)
        quick_sort(array, low, part-1)
        quick_sort(array, part+1, high)

def kth_largest(array, low, high, k):
    if low < high:
        part = partition(array, low, high)
        print(part)
        print(array)
        if part == k:
            print("came")
            print(array[part])
            return array[part]
        elif part < k:
            print('less')
            kth_largest(array, part+1, high, k)
        else:
            print('greater')
            kth_largest(array, low, part-1, k)

if __name__ == "__main__":
    a = [1,4,7,8,9,0,1,2,4,6,7,9,0,3,2,5,51,2,3,4,5,14,5,7,1]
    a = [2,1]
    #quick_sort(a, 0, len(a)-1)
    print(a)
    k = 2
    n = len(a) -1
    print(kth_largest(a, 0, n, n - k + 1))
    #quick_sort(a, 0, len(a)-1)
    print(a)
