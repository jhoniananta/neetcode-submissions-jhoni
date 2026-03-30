# Input: s = "AAABABB", k = 1

# Output: 5

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans = 0, 0
        count = {}
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(count[s[r]], max_freq)

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans



        