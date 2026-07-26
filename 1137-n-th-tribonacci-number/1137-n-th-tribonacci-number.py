class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        t,tt,ttt = 0,1,1
        for i in range(3, n+1):
            t,tt,ttt = tt, ttt, t+tt+ttt
        return ttt
        """
        :type n: int
        :rtype: int
        """
        