class Solution(object):
    def intersect(self, nums1, nums2):
        c = Counter(nums1)
        r = []
        for n in nums2:
            if c[n]>0:
                r.append(n)
            c[n]-=1
        return r
        

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        