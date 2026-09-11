class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        hold = -prices[0]
        sold = 0
        cool = 0

        for price in prices:
            hold, sold, cool = max(hold, cool - price), hold + price, max(cool, sold)
        
        return max(sold, cool)
