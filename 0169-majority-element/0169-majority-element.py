from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        c = Counter(nums)
        return c.most_common(1)[0][0]
        