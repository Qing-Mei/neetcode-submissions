class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = False, False, False

        for triplet in triplets:
            x |= (triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2])
            y |= (triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2])
            z |= (triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1])

            if x and y and z:
                return True
        
        return False
