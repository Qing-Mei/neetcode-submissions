import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x: x[0] ** 2 + x[1] ** 2

        def quickselect(left, right):
            if left >= right:
                return

            pivot = points[random.randint(left, right)]
            pivot_dist = dist(pivot)

            i = left
            l = left
            g = right

            while i <= g:
                curr_dist = dist(points[i])

                if curr_dist < pivot_dist:
                    points[i], points[l] = points[l], points[i]
                    i += 1
                    l += 1
                
                elif curr_dist > pivot_dist:
                    points[i], points[g] = points[g], points[i]
                    g -= 1
                
                else:
                    i += 1
            
            target = k - 1

            if target < l:
                quickselect(left, l - 1)
            else:
                quickselect(g + 1, right)

        quickselect(0, len(points) - 1)

        return points[:k]

