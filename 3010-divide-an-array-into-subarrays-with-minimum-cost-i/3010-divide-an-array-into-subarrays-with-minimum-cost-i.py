class Solution(object):
    def minimumCost(self, nums):
        m1 = float('inf')
        m2 = float('inf')
        for n in nums[1:]:
            if n<m1:
                m2 = m1
                m1 = n
            elif n<m2:
                m2 = n
        return nums[0] + m1 + m2
        """
        :type nums: List[int]
        :rtype: int
        """
        