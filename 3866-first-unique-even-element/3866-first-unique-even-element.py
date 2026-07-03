class Solution(object):
    def firstUniqueEven(self, nums):
        h = {}
        for n in nums:
            h[n] = h.get(n, 0)+1
        for n in nums:
            if n % 2 == 0 and h[n] == 1:
                return n
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
        