class Solution(object):
    def sortSentence(self, s):
        w = s.split()
        w.sort(key=lambda x: int(x[-1]))
        r = " ".join(wo[:-1] for wo in w)
        return r

        """
        :type s: str
        :rtype: str
        """
        