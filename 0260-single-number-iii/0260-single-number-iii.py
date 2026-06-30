class Solution(object):
    def singleNumber(self, nums):
        freq = defaultdict(int)  
        for n in nums:
            freq[n] += 1
        res = []
        for num, f in freq.items():
            if f == 1:
                res.append(num)
        return res
        # a = []
        # s = Counter(nums)
        # for i in nums:
        #     if s[i] == 1:
        #         a.append(i)
        # return a
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        