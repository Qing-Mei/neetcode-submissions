class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            next_prices = prices.copy()

            for from_, to, price in flights:
                if prices[from_] != float("inf"):
                    next_prices[to] = min(next_prices[to], prices[from_] + price)
            
            prices = next_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1
