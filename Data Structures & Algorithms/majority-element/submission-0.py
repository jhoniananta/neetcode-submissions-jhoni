from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums) // 2

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        most_val = max(count, key=count.get)
        # most_freq = count[most_val]

        return most_val
        

