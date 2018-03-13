def get_subsets(nums):
    if not nums:
        return []

    output = []
    import math
    counter = int(math.floor(math.pow(2, len(nums))))
    print(counter)
    for i in range(0, counter+1):
        temp = []
        for j in range(0, len(nums)):
            if i & (1 << j):
                temp.append(nums[j])
        output.append(temp)
    return output

print(get_subsets([1,2,3]))
