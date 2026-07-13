class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c = 0
        jewels = set([j for j in jewels])
        for s in stones:
            if s in jewels:
                c += 1
        return c
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        