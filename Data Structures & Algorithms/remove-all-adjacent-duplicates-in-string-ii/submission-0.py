class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, occurance]

        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if stack[-1][1] == k:
                stack.pop()
        
        res = []

        for i in stack:
            char = i[0]
            occur = i[1]
            res.append(char * occur)

        return "".join(res)