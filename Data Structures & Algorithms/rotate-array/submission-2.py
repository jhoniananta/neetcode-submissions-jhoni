class Solution:
    def swap(self, l: int, r: int, nums: List[int]):
        while l< r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # Reverse all the arrays
        l, r = 0, n - 1
        self.swap(l, r, nums)
        # Reverse the first portion
        l, r = 0, k - 1
        self.swap(l, r, nums)
        # Reverse the remaining portion
        l, r = k, n - 1
        self.swap(l, r, nums)