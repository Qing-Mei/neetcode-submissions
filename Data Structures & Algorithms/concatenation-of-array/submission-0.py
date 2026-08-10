class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * (n + n)

        for i, num in enumerate(nums):
            res[i], res[i + n] = num, num

        return res
