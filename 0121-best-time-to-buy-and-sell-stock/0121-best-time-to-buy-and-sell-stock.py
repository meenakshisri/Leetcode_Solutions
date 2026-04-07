class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_Price = float('inf')
        maxProfit = 0

        for price in prices:

            if price < min_Price:
                min_Price = price
            profit = price - min_Price

            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit



        