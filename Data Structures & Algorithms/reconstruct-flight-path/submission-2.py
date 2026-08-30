from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
    
        itinerary = []
        stack = ["JFK"]

        while stack:
            curr = stack[-1]
            if not graph[curr]:
                itinerary.append(stack.pop())
            else:
                stack.append(graph[curr].pop())
        
        return itinerary[::-1]
