class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1Idx = {num: i for i, num in enumerate(nums1)}
        # res = [-1] * len(nums1)

        # stack = []
        # for i in range(len(nums2)):
        #     cur = nums2[i]


        #     while stack and nums2[i] > stack[-1]:
        #         val = stack.pop()
        #         idx = nums1Idx[val]
        #         res[idx] = cur
        
        #     if cur in nums1Idx:
        #         stack.append(cur)
        # return res

        # different approach
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]