class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        up = [1] * n
        down = [1] * n

        max_len = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = down[i - 1] + 1
            elif arr[i] < arr[i - 1]:
                down[i] = up[i - 1] + 1
        
            max_len = max(max_len, up[i], down[i])
        
        return max_len
