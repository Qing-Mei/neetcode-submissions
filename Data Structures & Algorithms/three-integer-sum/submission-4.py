class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        nums.sort()

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        res = []

        n = len(nums)

        for i in range(n):
            seen[nums[i]] -= 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                seen[nums[j]] -= 1

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                need = -nums[i] - nums[j]

                if need in seen and seen[need] > 0:
                    res.append([nums[i], nums[j], need])
            
            for j in range(i + 1, n):
                seen[nums[j]] += 1

        return res
