class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        res = len(t)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                res -= 1
                j += 1
            i += 1
        
        return res
