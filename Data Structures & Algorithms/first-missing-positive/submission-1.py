class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(n):
            num = abs(nums[i])

            if 1 <= num <= n:
                if nums[num - 1] > 0:
                    nums[num - 1] *= -1
                elif nums[num - 1] == 0:
                    nums[num - 1] = -(n + 1)

        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
