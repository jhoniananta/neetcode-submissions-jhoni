class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]

        # Output: [-1,3,-1]

        # nums1Idx = {4:0, 1:1, 2:2} (num: i)

        # i = 0
        # Stack = [1,]

        # i = 1
        # cur = 3
        # Stack = [1, ]
        # Val = 1
        # idx = 1
        # res[1] = 3

        # i = 2
        # cur = 4
        # Stack = [1, ]
        # val = 1
        # idx =1
        # res[1] = 3


        for i in range(len(nums2)):
            cur = nums2[i]


            while stack and nums2[i] > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
        
            if cur in nums1Idx:
                stack.append(cur)
        return res