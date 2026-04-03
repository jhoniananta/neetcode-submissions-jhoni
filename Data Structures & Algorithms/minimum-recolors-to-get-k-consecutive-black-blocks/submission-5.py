class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = 0
        for i in range(k):
            if blocks[i] == 'W':
                count_w += 1

        res = count_w
        for r in range(k, len(blocks)):
            if blocks[r - k] == 'W':
                count_w -= 1
            if blocks[r] == 'W':
                count_w += 1
            res = min(res, count_w)
        
        return res