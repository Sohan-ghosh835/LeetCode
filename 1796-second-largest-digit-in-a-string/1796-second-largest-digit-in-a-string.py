class Solution(object):
    def secondHighest(self, s):
        n = "1234567890"
        d = []
        for i in range(len(s)):
            if s[i] in n:
                d.append(int(s[i]))
        d = set(d)
        if len(d) > 0:
            d.remove(max(d))
            if len(d) > 0:
                return max(d)
            else:
                return -1
        else:
            return -1


            

        """
        :type s: str
        :rtype: int
        """
        