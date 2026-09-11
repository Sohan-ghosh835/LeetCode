class Solution(object):
    def removeDuplicates(self, nums):
        b = []
        for ch in nums:
            if ch not in b:
                b.append(ch)
        for i in range(len(b)):
            nums[i] = b[i]
        return len(b)

        """
        :type nums: List[int]
        :rtype: int
        """
        