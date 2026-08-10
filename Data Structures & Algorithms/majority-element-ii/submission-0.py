class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candidate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
        
        res = []

        if cnt1 > len(nums) // 3:
            res.append(candidate1)
        
        if cnt2 > len(nums) // 3:
            res.append(candidate2)
        
        return res
        