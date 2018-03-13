class Solution:
    def comb_sum_helper(self, nums, target, current_sum, count):
        
        if current_sum > target:
            return
        
        if current_sum == target:
            count[0] += 1
        
        for i in range(0, len(nums)):
            self.comb_sum_helper(nums, target, current_sum + nums[i], count)
        
            
    
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        
        if target <= 0:
            return 0
        
        count = [0]
        self.comb_sum_helper(nums, target, 0, count)
        
        return count[0]

if __name__ == "__main__":
    s = Solution()
    c = s.combinationSum4([4,2,1], 32)
    print(c)
