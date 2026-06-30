class Solution(object):
    def singleNumber(self, nums):
        a = []
        s = Counter(nums)
        for i in nums:
            if s[i] == 1:
                a.append(i)
        return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        