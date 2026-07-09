class Solution(object):
    def sortColors(self, nums):
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        i = 0
        for _ in range(count[0]):
            nums[i] = 0
            i += 1
        for _ in range(count[1]):
            nums[i] = 1
            i += 1
        for _ in range(count[2]):
            nums[i] = 2
            i += 1


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        