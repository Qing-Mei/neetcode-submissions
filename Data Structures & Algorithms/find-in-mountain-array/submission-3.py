class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}

        l, r = 0, n - 1
        
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        if min(get(0), get(r)) > target:
            return -1

        while l < r:
            m = (l + r) // 2

            if get(m) < get(m + 1):
                l = m + 1
            else:
                r = m
        
        peak = l

        def binary_search(l, r, asc):
            while l <= r:
                m = (l + r) // 2
                val = get(m)

                if val == target:
                    return m
                elif (val < target) == asc:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        res = binary_search(0, peak, True)

        if res != -1:
            return res
        
        return binary_search(peak + 1, n - 1, False)
