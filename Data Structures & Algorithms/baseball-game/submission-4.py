class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            if c not in ["+", "D", "C"]:
                stack.append(int(c))
            else:
                if c == "+":
                    stack.append(int(int(stack[-1]) + int(stack[-2])))
                elif c == "C":
                    stack.pop()
                elif c == "D":
                    stack.append(int(int(stack[-1]) * 2))
        return sum(stack)
        