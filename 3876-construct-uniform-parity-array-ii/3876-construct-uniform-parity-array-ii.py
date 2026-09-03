class Solution(object):
    def uniformArray(self, nums1):
        return min(nums1)%2==1 or sum(x&1 for x in nums1)==0
        """
        :type nums1: List[int]
        :rtype: bool
        """
        