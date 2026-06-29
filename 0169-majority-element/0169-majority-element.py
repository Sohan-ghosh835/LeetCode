class Solution(object):
    def majorityElement(self, nums):
        cand = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                cand = n
            count += 1 if cand == n else -1
        return cand 
                
        """
        :type nums: List[int]
        :rtype: int
        """
        