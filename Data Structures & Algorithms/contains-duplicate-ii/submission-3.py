class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {} # {value, index} 
        for i in range(n):
            if nums[i] in mp and abs(i - mp[nums[i]]) <= k:
                return True
            else:
                mp[nums[i]] = i
        
        return False
