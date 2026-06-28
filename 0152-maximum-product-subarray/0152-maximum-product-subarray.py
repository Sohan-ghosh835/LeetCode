class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        cmin, cmax = 1,1
        for n in nums:
            if n == 0:
                cmin, cmax = 1,1
                continue
            tmp = cmax*n
            cmax = max(n*cmin, n*cmax, n)
            cmin = min(n*cmin, tmp, n)
            res = max(res, cmax)
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        