class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        candidates.sort()
        n = len(candidates)

        def dfs(start, target):
            if target == 0:
                res.append(path[:])
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                path.pop()
        
        dfs(0, target)

        return res
