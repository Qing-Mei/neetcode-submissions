class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r, k):
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
                
            if l >= r:
                return True
            
            if k == 0:
                return False
            
            if s[l] != s[r]:
                return helper(l + 1, r, k - 1) or helper(l, r - 1, k - 1)
        
        return helper(0, len(s) - 1, 1)
