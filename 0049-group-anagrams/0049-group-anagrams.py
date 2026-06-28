from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        gmap = defaultdict(list)
        res = []
        for s in strs:
            ss = tuple(sorted(s))
            gmap[ss].append(s)
        for value in gmap.values():
            res.append(value) 
        return res
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        