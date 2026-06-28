class Solution(object):
    def isPalindrome(self, s):
        ss = ""
        for ch in s:
            if ch.isalnum():
                ss += ch
        ss = ss.lower()
        sss = ss[::-1]
        return ss == sss
        """
        :type s: str
        :rtype: bool
        """
        