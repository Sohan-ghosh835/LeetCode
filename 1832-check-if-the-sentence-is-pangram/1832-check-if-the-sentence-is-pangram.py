class Solution(object):
    def checkIfPangram(self, sentence):
        n = "abcdefghijklmnopqrstuvwxyz"
        for ch in n:
            if ch  not in sentence:
                return False
        return True
        """
        :type sentence: str
        :rtype: bool
        """
        