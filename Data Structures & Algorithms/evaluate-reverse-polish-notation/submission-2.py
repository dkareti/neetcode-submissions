class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluate the rpn expression."""
        digits = []
        ans = 0
        
        for operand in tokens:
            if operand == "+":
                ans = digits.pop() + digits.pop()
                digits.append(ans)
            elif operand == "*":
                ans = digits.pop() * digits.pop()
                digits.append(ans)
            elif operand == "/":
                top, nxt = digits.pop(), digits.pop()
                ans = int(float(nxt) / top)
                digits.append(ans)
            elif operand == "-":
                top, nxt = digits.pop(), digits.pop()
                ans = nxt - top
                digits.append(ans)
            else:
                digits.append(int(operand))
        
        return digits[0]
