class Solution(object):
    def thirdMax(self, nums):
        s = set(nums)
        if len(s) < 3:
            return max(s)
        for _ in range(2):
            s.remove(max(s))
        return max(s)
        """
        :type nums: List[int]
        :rtype: int
        """
        