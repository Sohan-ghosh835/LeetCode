class Solution(object):
    def longestOnes(self, nums, k):
        maxx = 0
        nz = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                nz += 1
            while nz >k:
                if nums[l] == 0:
                    nz -= 1
                l += 1
            maxx = max(maxx, (r-l+1))
        return maxx
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        