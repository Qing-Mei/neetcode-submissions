from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
    
        itinerary = []
        def dfs(airport):
            while graph[airport]:
                destination = graph[airport].pop()
                dfs(destination)
            
            itinerary.append(airport)
        
        dfs("JFK")
        return itinerary[::-1]
