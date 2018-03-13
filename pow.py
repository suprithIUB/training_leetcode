class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        result = 1
        negative = False
        if n < 0:
            n = -n
            negative = True
        import pdb
        pdb.set_trace()
        while n:
            if n & 1:
                result = result * x
            n = n >> 1
            x = x * x
            
        if negative:
            return 1/result
        return result

if __name__ == "__main__":
    s = Solution()
    s.myPow(2, 5)
