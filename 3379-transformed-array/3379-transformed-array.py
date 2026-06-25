class Solution(object):
    def constructTransformedArray(self, nums):
        if not nums:
            return []
        n = len(nums)
        result = [0]*len(nums)
        for i in range(len(nums)):
            index = (i + nums[i]) % n
            result[i] = nums[index]
        return result