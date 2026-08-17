class Solution(object):
    def countDigits(self, num):
        if num<10 and num>0:
            return 1
        else:
            c = 0
            s = str(num)
            p = 0
            while p < len(s):
                if num%(int(s[p])) == 0:
                    c+=1
                p+=1
            return c
        """
        :type num: int
        :rtype: int
        """
        