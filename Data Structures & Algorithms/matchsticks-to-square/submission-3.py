class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)

        if n < 4 or total % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        target = total // 4

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return True
            
            tried = set()
            length = matchsticks[i]

            for side in range(4):
                if sides[side] in tried:
                    continue

                if sides[side] + length > target:
                    continue

                tried.add(sides[side])
                sides[side] += matchsticks[i]

                if dfs(i + 1):
                    return True

                sides[side] -= matchsticks[i]
            
            return False
        
        return dfs(0)
