class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        decoded = []
        length = 0
        i = 0
        n = len(s)

        while i < n:
            length = 0
            while i < n and s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
            
            i += 1
            word = s[i:i + length]
            i = i + length
            
            decoded.append(word)
        
        return decoded
