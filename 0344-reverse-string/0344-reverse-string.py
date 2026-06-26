class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
        return s
        """t
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        