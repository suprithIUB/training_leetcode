class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        if n <= 0:
            return ''
        if n == 1:
            return '1'
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)
        
        from collections import deque
        k_factoradic = deque()
        quotient = k-1
        counter = 1
        output = []
        while quotient:
            quotient, remainder = divmod(quotient, counter)
            k_factoradic.appendleft(remainder)
            counter += 1
        
        while len(k_factoradic) < len(numbers):
            k_factoradic.appendleft(0)
        
        for indx in k_factoradic:
            output.append(str(numbers[indx]))
            numbers = numbers[:indx] + numbers[indx+1:]
        
        print(k_factoradic)
        return ''.join(output)

if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(6, 349))
