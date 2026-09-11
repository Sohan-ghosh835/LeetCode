class Solution(object):
    def removeElement(self, nums, val):
        a = []
        for ch in nums:
            if ch != val:
                a.append(ch)
        for i in range(len(a)):
            nums[i] = a[i]
        return len(a)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        