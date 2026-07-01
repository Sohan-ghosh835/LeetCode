class Solution(object):
    def heightChecker(self, heights):
        c = sorted(heights)
        s = 0
        for i in range(len(heights)):
            if c[i] != heights[i]:
                s += 1
        return s


        """
        :type heights: List[int]
        :rtype: int
        """
        