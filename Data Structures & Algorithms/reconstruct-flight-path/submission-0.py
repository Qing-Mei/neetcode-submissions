from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)
    
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                destination = graph[airport].pop()
                dfs(destination)
            
            itinerary.append(airport)
        
        dfs("JFK")
        return itinerary[::-1]
