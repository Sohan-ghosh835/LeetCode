class Solution(object):
    def maxNumberOfBalloons(self, text):
        c = Counter(text)
        return min(c["b"], c["a"], c["l"] >> 1, c["o"] >> 1, c["n"])

        """
        :type text: str
        :rtype: int
        """
        