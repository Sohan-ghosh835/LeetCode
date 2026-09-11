class Solution(object):
    def mirrorDistance(self, n):
        s = str(n)
        s = s[::-1]
        return abs(n-int(s))
        """
        :type n: int
        :rtype: int
        """
        