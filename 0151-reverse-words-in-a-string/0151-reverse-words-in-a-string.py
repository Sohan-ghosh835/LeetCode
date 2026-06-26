class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        st = []
        for i in range(len(w) - 1, -1, -1):
            st.append(w[i])
        return " ".join(st)

        """
        :type s: str
        :rtype: str
        """
        