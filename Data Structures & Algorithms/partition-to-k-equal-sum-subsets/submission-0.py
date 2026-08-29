class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)

        if n < k or total % k != 0:
            return False
        
        nums.sort(reverse=True)
        target = total // k

        if nums[0] > target:
            return False

        subsets = [0] * k

        def dfs(i):
            if i == n:
                return True
            
            num = nums[i]
            tried = set()

            for sub in range(k):
                if subsets[sub] in tried:
                    continue
                    
                if subsets[sub] + num > target:
                    continue
                
                tried.add(subsets[sub])
                subsets[sub] += num

                if dfs(i + 1):
                    return True
                
                subsets[sub] -= num
            
            return False
        
        return dfs(0)
