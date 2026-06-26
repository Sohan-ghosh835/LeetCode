class Solution(object):
    def firstUniqChar(self, s):
        f = {}
        for ch in s:
            f[ch] = f.get(ch, 0) + 1
        for ch in s:
            if f[ch] == 1:
                return s.index(ch)
        return -1
        """
        :type s: str
        :rtype: int
        """
        