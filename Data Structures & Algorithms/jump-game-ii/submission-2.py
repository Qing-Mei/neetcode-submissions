from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            sz = len(q)

            for _ in range(sz):
                i = q.popleft()

                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    if j == n - 1:
                        return steps + 1

                    if j not in visited:
                        visited.add(j)
                        q.append(j)
            
            steps += 1
        
        return -1
