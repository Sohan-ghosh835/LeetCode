class Solution(object):
    def repeatedCharacter(self, s):
        sl = []
        for ch in s:
            if ch in sl:
                return ch
            sl.append(ch)
        return -1
        """
        :type s: str
        :rtype: str
        """
        