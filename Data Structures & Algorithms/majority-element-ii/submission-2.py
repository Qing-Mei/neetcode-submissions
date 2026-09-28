class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = {}

        for num in nums:
            if num not in cnt:
                cnt[num] = 0

            cnt[num] += 1
            
            if len(cnt) <= 2:
                continue
            
            new_cnt = {}
            for num, c in cnt.items():
                if c > 1:
                    new_cnt[num] = c - 1
        
            cnt = new_cnt

        res = []
        for num in cnt:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res
