class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if not nums_set:
            return 0

        num_to_i = {num: i for i, num in enumerate(nums_set)}

        n = len(nums_set)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]

            return size[root_x]
        
        res = 1

        for num in nums_set:
            idx = num_to_i[num]
            
            if num + 1 in nums_set:
                res = max(res, union(idx, num_to_i[num + 1]))
                    
        return res
