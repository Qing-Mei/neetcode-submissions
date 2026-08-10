class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
