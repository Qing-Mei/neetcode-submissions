class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bitwise_or = 0

        for num in nums:
            bitwise_or |= num
        
        return bitwise_or << (len(nums) - 1)
