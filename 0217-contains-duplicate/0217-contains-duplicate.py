class Solution(object):
    def containsDuplicate(self, nums):
        s = set(nums)
        if len(s)!=len(nums):
            return True
        return False
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        