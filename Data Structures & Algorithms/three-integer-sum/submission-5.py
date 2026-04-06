class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break

            # if i > 0 and a == nums[i-1]:
            #     continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    res.add(tuple([a, nums[l], nums[r]]))
                    l, r = l + 1, r - 1
        
        return [list(i) for i in res]
