class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key in counts.keys():
            if counts[key] > len(nums) // 3:
                res.append(key)
        
        return res