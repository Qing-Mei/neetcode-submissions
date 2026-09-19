class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3

        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)):
                continue
            
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True
                
            if all(found):
                return True
        
        return False
        