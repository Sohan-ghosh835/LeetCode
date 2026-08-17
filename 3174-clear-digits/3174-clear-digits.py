class Solution(object):
    def clearDigits(self, s):
        if s.isalpha():
            return s
        r = []
        for ch in s:
            if ch.isdigit():
                if r:
                    r.pop()
            else:
                r.append(ch)
        return "".join(r)

        """
        :type s: str
        :rtype: str
        """
        