class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minP = prices[0]
        maxProfit = 0

        for price in prices:
            profit = price - minP
            maxProfit = max(maxProfit, profit)
            minP = min(minP, price)
        
        return maxProfit

            

            
        