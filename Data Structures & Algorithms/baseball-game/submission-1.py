class Solution:
    def calPoints(self, operations: List[str]) -> int:

        temp = 0
        record = []
        
        for opr in operations:
            try:
                num = int(opr)
                record.append(num)
            except ValueError:
                if opr == "+":
                    num1 = int(record[-1])
                    num2 = int(record[-2])
                    record.append(num1 + num2)
                elif opr == "D":
                    num1 = int(record[-1])
                    record.append(2 * num1)
                elif opr == "C":
                    record.pop()
        
        return sum(record)


