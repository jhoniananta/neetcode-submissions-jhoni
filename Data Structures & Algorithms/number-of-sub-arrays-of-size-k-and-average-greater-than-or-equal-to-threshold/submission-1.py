class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefixSum[i + 1] += prefixSum[i] + arr[i]
        
        res = l = 0
        for r in range(k-1, len(arr)):
            sumWindow = prefixSum[r + 1] - prefixSum[l]
            if (sumWindow // k) >= threshold:
                res += 1
            l += 1
        return res

        