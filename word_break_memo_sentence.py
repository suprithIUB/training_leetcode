class Solution(object):
    def word_break_recur(self, s, word_dict, map_of_solved, output, level):
        if not s:
            return True, ''
        if s in map_of_solved:
            return False, ''
        i = 0
        while i <len(s):

            if s[0: i+1] in word_dict:
                ret_bool, ret_string = self.word_break_recur(s[i+1:], word_dict, map_of_solved, output, level+1)
                if ret_bool:
                    sentence = s[0: i+1] + " " + ret_string
                    if level == 0:
                        output.append(sentence.strip())
                        print(sentence)
                    else:
                        return True, sentence
            i += 1

        if level == 0 and i == len(s) and output:
            return True, ''

        map_of_solved.add(s)
        return False, None

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        d = set(wordDict)
        map_of_solved  = set()
        output = []
        self.word_break_recur(s, d, map_of_solved, output, 0)
        return output

if __name__ == "__main__":
    sol = Solution()
    word = "aaaaaaa"
    li = ["aaaa","aa"]
    print(sol.wordBreak(word, li))
