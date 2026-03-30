class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        for i in range(len(s)):
            freq_map = {}
            maxf = 0
            for j in range(i, len(s)):
                freq_map[s[j]] = 1 + freq_map.get(s[j], 0)
                maxf = max(maxf, freq_map[s[j]])
                if (( j- i + 1) - maxf ) <= k:
                    res = max(j-i+1, res)

        return res

        