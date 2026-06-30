class Solution(object):
    def topKFrequent(self, words, k):
        c = Counter(words)
        return sorted(c.keys(), key=lambda w: (-c[w], w))[:k]
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        