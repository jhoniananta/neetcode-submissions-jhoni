class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        res = 1

        for i in range(n):
            l, r = 0, i
            while l <= r:
                m = (l + r) // 2
                curSum = prefixSum[i + 1] - prefixSum[m]
                need = (i - m + 1) * nums[i] - curSum
                if need <= k:
                    r = m - 1
                    res = max(res, i - m + 1)
                else:
                    l = m + 1
        
        return res