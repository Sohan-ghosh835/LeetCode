class Solution(object):
    def sortedSquares(self, nums):
        a = []
        for i in range(len(nums)):
            a.append(nums[i]**2)
        a = sorted(a)
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        