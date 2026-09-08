class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total & 1:
            return False
        
        nums.sort()

        def backtrack(start, target):
            if target == 0:
                return True
            
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                
                if backtrack(i + 1, target - nums[i]):
                    return True
            
            return False
        
        return backtrack(0, total // 2)
