class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False
        
        max_num = max(nums)

        spf = list(range(max_num + 1))

        for prime in range(2, int(max_num ** 0.5) + 1):
            if prime == spf[prime]:
                for multiple in range(prime * prime, max_num + 1, prime):
                    if spf[multiple] == multiple:
                        spf[multiple] = prime

        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(x, y):
            nonlocal components

            root_x = parent[x]
            root_y = parent[y]

            if root_x == root_y:
                return
            
            if size[root_y] > size[root_x]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]
            components -= 1
        
        prime_owner = {}

        for i, val in enumerate(nums):
            num = val

            while num > 1:
                prime = spf[num]

                if prime in prime_owner:
                    union(i, prime_owner[prime])
                else:
                    prime_owner[prime] = i
                
                while num % prime == 0:
                    num //= prime
        
        return components == 1









