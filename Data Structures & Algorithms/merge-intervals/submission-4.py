class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort(key=lambda x: (x[0], -x[1]))

        res = []
        active = 0
        start = 0

        for pos, change in events:
            if active == 0:
                start = pos
            
            active += change

            if active == 0:
                res.append((start, pos))
        
        return res
