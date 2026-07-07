class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res, sol = [], []
        def bcktr(i):
            if i == n:
                res.append(sol[:])
                return
            bcktr(i+1)
            sol.append(nums[i])
            bcktr(i+1)
            sol.pop()
        bcktr(0)
        return res


            

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        