class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == ")" or ch == "}" or ch == "]":
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (ch == ")" and top != "(") or (ch == "}" and top != "{") or (ch == "]" and top != "["):
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
        
        

        """
        :type s: str
        :rtype: bool
        """
        