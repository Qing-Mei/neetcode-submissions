class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        target = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False
        
        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True

            length = matchsticks[i]

            for side in range(4):
                if sides[side] + length > target:
                    continue
                
                sides[side] += length

                if dfs(i + 1):
                    return True
            
                sides[side] -= length

                if sides[side] == 0:
                    break
        
            return False
        
        return dfs(0)
