class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)

        prev1 = 1
        prev2 = 1

        for i in range(1, n):
            curr = 0
            # s[i - 1] x 
            if s[i] != "0":
                curr += prev1
            
            two_digit = int(s[i-1:i+1])
            # s[i-2] x
            if 10 <= two_digit <= 26:
                curr += prev2
            
            prev2, prev1 = prev1, curr
        
        return prev1
        