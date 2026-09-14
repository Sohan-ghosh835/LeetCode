class Solution(object):
    def isRectangleOverlap(self, r1, r2):
        return min(r1[2],r2[2])>max(r1[0], r2[0]) and min(r1[3],r2[3])>max(r1[1], r2[1])
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        