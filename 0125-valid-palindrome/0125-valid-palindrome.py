class Solution(object):
    def isPalindrome(self, s):
        ss  = ""
        for ch in s:
            if ch.isalnum():
                ss += ch
        ss = ss.lower()
        t = ss[::-1]
        if ss == t:
            return True
        else:
            return False
            
        """
        :type s: str
        :rtype: bool
        """
        