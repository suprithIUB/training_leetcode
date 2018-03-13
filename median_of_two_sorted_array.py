import pdb
def median_of_two_sorted_arrays(a, b):
    if len(b) < len(a):
        a, b = b, a

    pdb.set_trace()
    x = len(a)
    y = len(b)
    low = 0
    high = x
    import sys
    
    while low <=high:
        part_x = (low + high)//2
        part_y = ((x+y+1)//2) - part_x
        
        x_left_max = -sys.maxsize -1 if part_x == 0 else a[part_x-1]
        x_right_min = sys.maxsize if part_x == x else a[part_x]
        
        
        y_left_max = -sys.maxsize -1 if part_y == 0 else b[part_y-1]
        y_right_min = sys.maxsize if part_y == y else b[part_y]

        if x_left_max <= y_right_min and y_left_max <= x_right_min:
            if (x + y) % 2 == 0:
                return (min(x_right_min, y_right_min) + max(x_left_max,y_left_max))/2
            else:
                return max(x_left_max, y_left_max)
        elif x_left_max > y_right_min:
            high = part_x-1
        else:
            low = part_x+1

if __name__=="__main__":
    a = [2,5,7,9]
    b = [1,3,4,5,7,8,9]

    median = median_of_two_sorted_arrays(a, b)
    sorted_merge = []
    low1= 0
    low2 = 0
    while low1 < len(a) and low2 < len(b):
        if a[low1] < b[low2]:
            sorted_merge.append(a[low1])
            low1 += 1
        elif a[low1] > b[low2]:
            sorted_merge.append(b[low2])
            low2 += 1
        else:
            sorted_merge.append(a[low1])
            sorted_merge.append(b[low2])
            low1 += 1
            low2 += 1

    while low2 < len(b):
        sorted_merge.append(b[low2])
        low2 += 1
    print(sorted_merge)
    mid = (0 + len(sorted_merge) -1)// 2
    assert(sorted_merge[mid] == median)
