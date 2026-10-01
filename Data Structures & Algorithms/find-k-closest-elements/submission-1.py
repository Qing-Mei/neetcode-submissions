class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if arr[m] <= x:
                l = m + 1
            else:
                r = m

        if 0 < l and abs(arr[l] - x) >= abs(x - arr[l - 1]):
            l = l - 1
        
        r = l
        while r - l + 1 < k:
            if r == n - 1:
                l -= 1
                continue
            elif l == 0:
                r += 1
                continue

            if abs(arr[l - 1] - x) <= abs(arr[r + 1] - x):
                l -= 1
            else:
                r += 1

        return arr[l:r+1]
