class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        if nums[0] >= len(nums)-1:
            return True
        
        if nums[0] == 0:
            return False
        
        max_heap = []
        import heapq
        max_heap.append((-nums[0],-nums[0],0))
        while max_heap:
            _, max_, i = heapq.heappop(max_heap)
            max_heap = []
            max_ = -max_
            i = -i
            limit = i + max_
            #print(limit)
            if limit >= len(nums)-1:
                return True
            
            i += 1
            while(i <= limit):
                heapq.heappush(max_heap, ( -(nums[i] + i), -nums[i], -i))
                i+= 1
            #print(max_heap)
        return False

if __name__ == "__main__":
    s = Solution()
    test = [1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0] 
    print(s.canJump(test))
