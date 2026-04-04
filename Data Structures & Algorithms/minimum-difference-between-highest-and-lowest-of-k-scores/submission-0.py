class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, k - 1

        res = float("inf")
        
        while r < len(nums):
            diff = nums[r] - nums[l]
            res = min(res, diff)
            l, r = l + 1, r + 1

        return res