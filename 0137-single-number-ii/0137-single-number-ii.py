class Solution(object):
    def singleNumber(self, nums):
        s = Counter(nums)
        for i in nums:
            if s[i] == 1:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        