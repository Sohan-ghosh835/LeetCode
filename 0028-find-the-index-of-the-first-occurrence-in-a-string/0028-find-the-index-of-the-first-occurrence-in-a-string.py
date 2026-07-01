class Solution(object):
    def strStr(self, haystack, needle):
        l = 0
        while l <= len(haystack) - len(needle):
            r = 0
            c = 0
            while r<len(needle):
                if haystack[l+r] == needle[r]:
                    c += 1
                    r += 1
                else:
                    break
            if c == len(needle):
                return l
            l+=1
        return -1




        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        