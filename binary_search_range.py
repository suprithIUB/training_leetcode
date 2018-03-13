class Solution:

    def search_helper(self, nums, target):
        #ceil of element
        low = 0
        high = len(nums)-1
        result = -1
        out = [-1, -1]
        while low <= high:
            mid = low + (high - low) //2
            if nums[mid] <= target:
                low = mid+1
            else:
                result = mid
                high = mid-1
        if result != -1:
            out[1] = result-1
        else:
            out[1] = len(nums)-1

        high = out[1]
        low =0
        
        # first occurence
        while low <=high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                result = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1
        out[0] = result
        return out
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        
        result = self.search_helper(nums, target)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([0,0,0,0,0], 0))
