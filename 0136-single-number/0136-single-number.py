class Solution(object):
    def singleNumber(self, nums):
        if len(nums) <= 1:
            return nums[0]
        s = Counter(nums)
        for n in s:
            if s[n] == 1:
                return n
            
            
            

        
        """
        :type nums: List[int]
        :rtype: int
        """
        