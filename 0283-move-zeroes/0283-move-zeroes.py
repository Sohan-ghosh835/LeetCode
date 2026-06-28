class Solution(object):
    def moveZeroes(self, nums):
        c = 0
        arr = []
        for n in nums:
            if n == 0:
                c+=1
            else:
                arr.append(n)
        arr.extend([0] * c)
        nums[:] = arr

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        