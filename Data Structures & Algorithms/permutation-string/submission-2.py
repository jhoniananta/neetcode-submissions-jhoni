class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False
        
        s1Map ={}
        windowMap = {}

        for ch in s1:
            s1Map[ch] = s1Map.get(ch, 0) + 1
        
        for i in range(k):
            ch = s2[i]
            windowMap[ch] = windowMap.get(ch, 0) + 1

        if s1Map == windowMap:
            return True

        # Sliding window

        for r in range(k, n):
            addChar = s2[r]
            removeChar = s2[r - k]

            windowMap[addChar] = windowMap.get(addChar, 0) + 1
            windowMap[removeChar] -= 1

            if windowMap[removeChar] == 0:
                del windowMap[removeChar]

            if s1Map == windowMap:
                return True

        
        return False
