class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        output, n = [], len(nums)

        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            if (j-i) > n // 3:
                output.append(nums[i])
            i = j
        
        return output