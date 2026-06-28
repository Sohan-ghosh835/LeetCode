class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = l+1
        m = 0
        while r< len(prices):
            if prices[l]<prices[r]:
                m = max(m, prices[r]-prices[l])
            else:
                l = r
            r+=1
        return m





        """
        :type prices: List[int]
        :rtype: int
        """
        