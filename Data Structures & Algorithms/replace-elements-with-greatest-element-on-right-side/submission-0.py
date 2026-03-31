class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        output = [0] * n

        for i in range(n):
            rightMax = -1
            for j in range(i+1, n):
                rightMax = max(rightMax, arr[j])
            output[i] = rightMax
        
        return output