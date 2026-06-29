class Solution(object):
    def isHappy(self, n):
        s = set()
        c = str(n)
        while c not in s:
            s.add(c)
            su = 0
            for d in c:
                d = int(d)
                su += d**2
            if su == 1:
                return True
            c = str(su)
        return False

        """
        :type n: int
        :rtype: bool
        """
        