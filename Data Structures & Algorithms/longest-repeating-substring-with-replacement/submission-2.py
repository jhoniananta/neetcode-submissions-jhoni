# Input: s = "AAABABB", k = 1

# Output: 5

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            count = {}
            max_freq = 0

            for j in range(i, n):
                count[s[j]] = 1 + count.get(s[j], 0)
                max_freq = max(max_freq, count[s[j]])

                window_len = j - i + 1
                replacement_needed = window_len - max_freq

                if replacement_needed <= k:
                    ans = max(window_len, ans)

        return ans



        