class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        l1, r1 = 0, m

        while l1 <= r1:
            m1 = (l1 + r1) // 2
            m2 = (m + n) // 2 - m1

            left_nums1 = nums1[m1 - 1] if m1 > 0 else float("-inf")
            right_nums1 = nums1[m1] if m1 < m else float("inf")

            left_nums2 = nums2[m2 - 1] if m2 > 0 else float("-inf")
            right_nums2 = nums2[m2] if m2 < n else float("inf")

            if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
                if (m + n) & 1:
                    return min(right_nums1, right_nums2)
                else:
                    return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2
            
            elif left_nums1 > right_nums2:
                r1 = m1 - 1

            else:
                l1 = m1 + 1
