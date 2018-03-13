class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
    
        result_set = set()
        nums.sort()
        
        i = 0
        
        while i < len(nums)-2:
            a = nums[i]

            start = i+1
            end = len(nums)-1
            
            while start < end:
                b = nums[start]
                c = nums[end]
                if (a + b + c) == 0:
                    result_set.add((a, b, c))
                    if b == nums[start+1]:
                        start = start +1
                    else:
                        end = end-1
                elif (a + b + c) > 0:
                    end -= 1
                else:
                    start += 1
            i += 1    
        return list(result_set)

if __name__ =="__main__":
    import csv
    sol = Solution()
    with open("large_array.csv") as f:
        #print(row)
        array = []
        for item in  csv.reader(f, delimiter=','):
            array = [int(num) for num in item]
        print(sol.threeSum(array))
