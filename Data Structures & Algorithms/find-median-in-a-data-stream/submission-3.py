import heapq

class MedianFinder:

    def __init__(self):
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.upper or self.upper[0] <= num:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)
        
        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper)) 
        elif len(self.lower) > len(self.upper):
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return self.upper[0]

        return (self.upper[0] - self.lower[0]) / 2        
        