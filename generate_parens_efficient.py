class Solution:

    def helper(self, left_rem, right_rem, current_paren_array, indx, parens_list):

        if left_rem < 0 or right_rem < left_rem: # invalid string
            return
        if left_rem == 0 and right_rem == 0:
            new_parens = ''.join(current_paren_array)
            parens_list.append(new_parens)
            return
        else:
            if left_rem > 0:
                current_paren_array[indx] = "("
                self.helper(left_rem-1, right_rem, current_paren_array, indx+1, parens_list)
            if right_rem > left_rem:
                current_paren_array[indx] = ")"
                self.helper(left_rem, right_rem-1, current_paren_array, indx+1, parens_list)

        return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        current_paren_array = []
        for i in range(0, 2*n + 1):
            current_paren_array.append("")
            parens_list = []
        self.helper(n, n, current_paren_array, 0, parens_list)

        return parens_list

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))

    print(sol.generateParenthesis(5))
    
