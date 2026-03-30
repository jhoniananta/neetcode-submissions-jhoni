class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums = [1,0,1,2]
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                i -= 1
                r -= 1
            i += 1


        