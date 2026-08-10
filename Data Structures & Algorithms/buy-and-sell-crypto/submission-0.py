class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for p in prices:
            max_profit = max(max_profit, p - lowest_price)
            lowest_price = min(lowest_price, p)
        
        return max_profit
        