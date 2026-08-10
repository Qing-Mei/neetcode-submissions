class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. brute force 3 layer for loop pick i, j, k time O(n^3) space O(1)
        # 2. hashmap time O(n^2) space O(n)
        # 3. sort time O(nlogn) for pick up i, inner for loop two pointer j and k
        # time O(n^2) space O(1)

        nums.sort()

        ans = []
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            if nums[i] > 0:
                break
            
            if nums[i] + nums[n - 1] + nums[n - 2] < 0:
                continue

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return ans
