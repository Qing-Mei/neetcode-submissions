class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                s = strs[j]
                if i == len(s) or ch != s[i]:
                    return strs[0][:i]
        
        return strs[0]
