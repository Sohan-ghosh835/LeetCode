class Solution(object):
    def missingNumber(self, nums):
        l = len(nums)
        c = 0
        for i in range(1, l+1):
            c += i
        return c-sum(nums)
            
        
            


        """
        :type nums: List[int]
        :rtype: int
        """
        