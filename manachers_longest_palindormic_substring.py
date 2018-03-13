class Solution:
    
    def add_sentinels(self, s):
        ret = "^"
        for c in s:
            ret += "#" + c
        ret += "#$"
        print(ret)
        return ret
    
    def find_string(self, result, s):
        max_len = 0
        center = 0
        #print(result)
        for i in range(0, len(result)):
            if result[i] > max_len:
                max_len = result[i]
                center = i
        print(center, max_len)
        start = (center -1 -max_len)//2
        
        return s[start: start+max_len]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        t = self.add_sentinels(s)
        result = list()
        for i in range(0, len(t)):
            result.append(0)
        
        center = 0
        edge = 0
        for i in range(1, len(t)-1):
            mirror_i = 2*center -i
            
            result[i] = min((edge-i), result[mirror_i]) if edge > i else 0
            
            while (t[result[i] + i +1] == t[i - 1 - result[i]]):
                result[i] += 1
            if (result[i] > (center - edge)):
                center = i
                edge = i + result[i]
        
        return self.find_string(result, s)

if __name__ == "__main__":
    string = "babad"
    sol = Solution()
    import pdb
    pdb.set_trace()
    print(sol.longestPalindrome(string))
