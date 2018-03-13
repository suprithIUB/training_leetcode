class Solution:

    def add_sentinels(self, s):
        ret = "^#"
        for c in s:
            ret += c + "#"
        ret += "^"

        print(ret)
        return ret

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        t = self.add_sentinels(s)
        print(len(t))
        result = 0
        from_indx = 0
        end_indx = 0
        for i in range(0, len(t)):
            center = i
            low  = center
            high = center
            while t[low] != "^" and t[high] != "^":
                if t[low] == t[high]:
                    low -= 1
                    high += 1
                else:
                    break

            if (high - low) > result:
                print("updating result %s %s %s"%(high, low, center))
                result = high - low
                from_indx = low+1
                end_indx = high-1

        print(t[from_indx: end_indx])
        print()
        return s[from_indx//2: end_indx//2]

if __name__ == "__main__":
    sol = Solution()
    s = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    print("sup %s"%len(s))
    sol.longestPalindrome(s)
