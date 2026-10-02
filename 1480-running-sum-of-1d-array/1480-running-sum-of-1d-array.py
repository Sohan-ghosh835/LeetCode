class Solution(object):
    def runningSum(self, nums):
        s = 0
        a = []
        for i in range(len(nums)):
            s += nums[i]
            a.append(s)
        return a


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        