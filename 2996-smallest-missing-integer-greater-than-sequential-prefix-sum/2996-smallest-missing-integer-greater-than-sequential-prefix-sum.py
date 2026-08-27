class Solution(object):
    def missingInteger(self, nums):
        i = 0
        j = 0
        s = nums[0]
        while j < len(nums) - 1:
            if nums[j] + 1 == nums[j + 1]:
                s += nums[j + 1]
                j += 1
            else:
                break
        while s in nums:
            s += 1
        return s
            
            

        """
        :type nums: List[int]
        :rtype: int
        """
        