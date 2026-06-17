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


        