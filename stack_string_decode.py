class Solution(object):
    
    def append_digit(self, current, new_digit):
        new_current = current * 10
        new_current += new_digit
        print(new_current)
        return new_current
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        from collections import deque
        stack = deque()
        number_mapper = {'0': 0, '1':1, '2':2, '3': 3, '4': 4,
                        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        
        indx = 0
        while indx < len(s):
            if s[indx] in number_mapper:  
                
                if stack and isinstance(stack[-1], int):
                    print(stack[-1])
                    print("getting numbers with multiple digits")
                    new_num = self.append_digit(stack.pop(), number_mapper[s[indx]])
                    stack.append(new_num)
                else:
                    stack.append(number_mapper[s[indx]])
            
            elif s[indx] == ']':
                number = 0
                temp_str = deque()
                while stack:
                    print('popping')
                    stack_top = stack.pop()
                    if stack_top == '[':
                        number = stack.pop()
                        print(temp_str) 
                        stack.append(''.join(temp_str) * number)
                        break
                    else:
                        temp_str.appendleft(stack_top)
                
            else:
                stack.append(s[indx])
            print(stack)
            indx += 1
        
        return ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("100[suprith]"))
    
