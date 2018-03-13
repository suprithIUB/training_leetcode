class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        ugly_numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

        pointers = [-1, -1, 6, 4, -1, 2]
        prime_factors = [2,3,5]
        import sys
        current_lowest = 12
        lowest_array = [sys.maxsize,sys.maxsize,12,12,sys.maxsize,12]
        while len(ugly_numbers) < n:
            for prime in prime_factors:
                for i in range(pointers[prime], len(ugly_numbers)):
                    temp = prime * ugly_numbers[i]
                    if temp > lowest_array[prime]:
                        lowest_array[prime] = temp
                        break

            next_ugly = min(min(lowest_array[2], lowest_array[3]), lowest_array[5])
            #print(next_ugly)
            pointers[lowest_array.index(next_ugly)] += 1
            #print(pointers)
            lowest_array[2] = lowest_array[3] = lowest_array[5] = next_ugly
            ugly_numbers.append(next_ugly)

        return ugly_numbers[n-1]

if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(1069))

