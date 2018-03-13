class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        if k < 1 or t < 0:
            return False
        
        from collections import OrderedDict
        d = OrderedDict()
        
        for n in nums:
            bucket = n//t if t else n
            for pair in (d.get(bucket-1), d.get(bucket), d.get(bucket+1)):
                print(pair, n)
                if pair is not None and abs(n - pair) <= t:
                    return True
            
            if len(d) == k and d:
                d.popitem(False)
            d[bucket] = n
        
        return False


