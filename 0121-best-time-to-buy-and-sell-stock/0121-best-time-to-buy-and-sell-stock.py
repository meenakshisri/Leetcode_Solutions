class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for sell in prices:
            maxProfit = max(maxProfit, sell - minPrice)
            minPrice = min(minPrice, sell)
        return maxProfit

        

                
        