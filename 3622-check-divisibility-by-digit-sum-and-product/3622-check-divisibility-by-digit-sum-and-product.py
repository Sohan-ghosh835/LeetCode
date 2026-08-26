class Solution(object):
    def checkDivisibility(self, n):
        if n<10:
            return False
        t = n
        s = 0
        p = 1
        while n != 0:
            d = n%10
            s += d
            p *= d
            n //= 10
        if t%(s+p) == 0:
            return True
        else:
            return False


        """
        :type n: int
        :rtype: bool
        """
        