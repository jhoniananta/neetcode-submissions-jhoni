class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0

        windowSumAvg = sum(arr[:k]) // k
        if windowSumAvg >= threshold: 
            res += 1
        for r in range(k, len(arr)):
            windowSumAvg += (arr[r] - arr[r  - k]) // k
            if windowSumAvg >= threshold:
                res += 1
        
        return res