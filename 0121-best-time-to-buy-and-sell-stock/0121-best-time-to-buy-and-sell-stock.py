class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        l = 0 #buy
        r = 1 #sell
        maxProfit = 0

        for r in range(len(prices)):

            profit = prices[r]-prices[l]
            if profit<0:
                l = r
            else:            
                maxProfit = max(maxProfit, profit)
        return maxProfit

        """
        l = 0 #buy
        r = 1 #sell
        maxProfit = 0

        while r<len(prices):

            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            
            r +=1
        
        return maxProfit
        """
 

        
