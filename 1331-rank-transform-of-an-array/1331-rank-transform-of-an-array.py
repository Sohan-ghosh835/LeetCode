class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}
        for a in sorted(arr):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, arr)
        
       

        """
        :type arr: List[int]
        :rtype: List[int]
        """
        