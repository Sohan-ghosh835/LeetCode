class Solution(object):
    def dominantIndex(self, nums):
        m  = max(nums)
        c = 0
        ii = nums.index(m)
        nums.sort()
        for i in range(len(nums)-1):
            if m >= 2*nums[i]:
                c+=1
            else:
                continue
        if c != len(nums)-1:
            return -1
        else:
            return ii

        """
        :type nums: List[int]
        :rtype: int
        """
        