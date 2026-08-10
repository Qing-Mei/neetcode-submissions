class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(i, j, k):
            if i == len(nums1):
                return nums2[j + k - 1]
            
            if j == len(nums2):
                return nums1[i + k - 1]
            
            if k == 1:
                return min(nums1[i], nums2[j])
            
            half = k // 2

            i_nxt = min(i + half, len(nums1)) - 1
            j_nxt = min(j + half, len(nums2)) - 1

            if nums1[i_nxt] > nums2[j_nxt]:
                removed = j_nxt - j + 1
                return get_kth(i, j_nxt + 1, k - removed)
            else:
                removed = i_nxt - i + 1
                return get_kth(i_nxt + 1, j, k - removed)
        
        total = len(nums1) + len(nums2)

        if total & 1:
            return get_kth(0, 0, total // 2 + 1)
        
        return (get_kth(0, 0, total // 2) + get_kth(0, 0, total // 2 + 1)) / 2
