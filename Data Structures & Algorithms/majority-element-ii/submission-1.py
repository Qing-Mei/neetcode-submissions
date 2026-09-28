class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = cnt2 = 0
        can1, can2 = None, None

        for num in nums:
            if num == can1:
                cnt1 += 1
            elif num == can2:
                cnt2 += 1
            elif cnt1 == 0:
                can1 = num
                cnt1 = 1
            elif cnt2 == 0:
                can2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0

        for num in nums:
            if num == can1:
                cnt1 += 1
            elif num == can2:
                cnt2 += 1
        
        res = []

        if cnt1 > len(nums) // 3:
            res.append(can1)
        
        if cnt2 > len(nums) // 3:
            res.append(can2)
        
        return res
