#Runtime: O(n)
#Space: O(n)
class Solution(object):
    #shunting yard algorithm
    def get_rpn(self, s):
        if not s:
            return ''
        output_queue = []
        operator_stack = []
        precedence = {'-': 2, '+': 2, '*': 3, '/': 3}
        
        indx = 0
        prev_num = False
        while indx < len(s):
            c = s[indx]
            
            if c == '*' or c == '+' or c == '-' or c == '/':
                while operator_stack and operator_stack[-1] != '(' and precedence[c] <= precedence[operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(c)
                prev_num = False
            elif c == '(':
                operator_stack.append(c)
                prev_num = False
            elif c == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
                prev_num = False
            elif c != ' ':
                if not prev_num:
                    prev_num = True
                    output_queue.append(c)
                else:
                    num = int(output_queue[-1])
                    output_queue.pop()
                    num *= 10
                    num += int(c)
                    output_queue.append(str(num))
            indx += 1
        
        while operator_stack:
            output_queue.append(operator_stack.pop())
        return output_queue
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        rpn = self.get_rpn(s.encode('utf-8'))
        #print(rpn)
        stack = []
        
        indx = 0
        while indx < len(rpn):
            c =  rpn[indx]
            if c == '*' or c == '+' or c == '-' or c == '/':
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = None
                if c == '*':
                    result = operand_1 * operand_2
                elif c == '+':
                    result = operand_1 + operand_2
                elif c == '-':
                    result = operand_1 - operand_2
                elif c == '/':
                    result = operand_1 // operand_2
                stack.append(result)
            else:
                stack.append(int(c))
            indx += 1
        
        return stack[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
