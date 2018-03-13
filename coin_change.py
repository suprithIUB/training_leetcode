class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if not coins:
            return -1
        matrix = [(amount+1) for _ in range(0, amount+1)]
        
        matrix[0] = 0
        for coin in coins:
            for i in range(0, len(matrix)):
                if i >= coin:
                    matrix[i] = min(matrix[i], (matrix[i-coin] + 1))

        if matrix[-1] == (amount+1):
            return -1
        return matrix[-1]

if __name__ == "__main__":
    s = Solution()
    l = [94,485,208,129,301,312,479,254]
    num = 4589
    b = s.coinChange(l, num)
    print(b)
