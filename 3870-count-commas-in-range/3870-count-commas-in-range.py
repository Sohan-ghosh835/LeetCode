class Solution(object):
    def countCommas(self, n):
        d = 0
        if len(str(n)) >= 4:
            d = (n-1000)+1
        return d

        """
        :type n: int
        :rtype: int
        """
        