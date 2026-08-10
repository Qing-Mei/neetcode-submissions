class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []
        self.days = []
        self.index = 0

    def next(self, price: int) -> int:
        day = 1

        while self.stack and self.prices[self.stack[-1]] <= price:
            day += self.days[self.stack.pop()]

        self.days.append(day)
        self.prices.append(price)
        self.stack.append(self.index)
        self.index += 1

        return day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)