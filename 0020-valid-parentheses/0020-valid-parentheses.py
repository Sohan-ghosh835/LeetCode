class Solution(object):
    def isValid(self, s):
        stack = []
        n = "({["
        for ch in s:
            if ch in n:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if  (ch == ')' and top != '(') or \
                    (ch == ']' and top != '[') or \
                    (ch == '}' and top != '{'):
                        return False
        return len(stack) == 0
       
        
        

        """
        :type s: str
        :rtype: bool
        """
        