class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        st = []
        for i in range(0, len(w)):
            st.append("".join(reversed(w[i])))
        return " ".join(st)
        """
        :type s: str
        :rtype: str
        """
        