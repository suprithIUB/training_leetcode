class Solution:
    def lengthOfLongestSubstring_linear(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        longest_len = 0
        last_start = 0
        char_set = set()
        indx = 0
        while indx < len(s):
            if s[indx] not in char_set:
                char_set.add(s[indx])
                longest_len += 1
                indx+= 1
                if max_len < longest_len:
                    max_len = longest_len
            else:
                print(char_set)
                clash_char = s[indx]
                print ("indx%s"%indx)
                while last_start < indx and clash_char in char_set:
                    char_set.remove(s[last_start])
                    print("after remv")
                    print(char_set)
                    last_start += 1
                    longest_len -= 1
                    print(last_start)
        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        char_set = set()
        for i in range(0, len(s)):
            start = i
            for j in range(start, len(s)):
                if s[j] in char_set:
                    if (j-start) > longest_len:
                        longest_len = (j- start)
                        char_set.clear()
                    break
                else:
                    char_set.add(s[j])
        return longest_len

if __name__=="__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring_linear("abcabcbb"))

