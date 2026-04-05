class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")

        l = 0
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]

            while curSum >= target:
                curWindowSize = r - l + 1
                minLength = min(minLength, curWindowSize)

                curSum -= nums[l]
                l += 1
            
        if minLength == float("inf"):
            return 0
        else:
            return int(minLength)