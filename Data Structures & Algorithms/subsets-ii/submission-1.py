class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        prev_size = 0

        for i in range(len(nums)):
            curr_size = len(res)

            if i > 0 and nums[i] == nums[i - 1]:
                start = prev_size
            else:
                start = 0

            for j in range(start, curr_size):
                res.append(res[j] + [nums[i]])
            
            prev_size = curr_size

        return res
