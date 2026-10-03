class Solution(object):
    def moveZeroes(self, nums):
        s = []
        c = 0
        for ch in nums:
            if ch == 0:
                c += 1
            else:
                s.append(ch)
        for i in range(c):
            s.append(0)
        nums[:] = s

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        