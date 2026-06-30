class Solution(object):
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        ans = [num for num, freq in c.most_common(k)]
        return ans

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        