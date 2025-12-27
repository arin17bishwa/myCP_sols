from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate(op1: int, op2: int, operator: str) -> int:
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            else:
                return int(op1 / op2)

        arr = tokens
        n = len(arr)
        q: deque[int] = deque()

        for ele in arr:
            if ele in "+-*/":
                operand2 = q.pop()
                operand1 = q.pop()
                q.append(evaluate(operand1, operand2, ele))
            else:
                q.append(int(ele))
        return q.pop()
