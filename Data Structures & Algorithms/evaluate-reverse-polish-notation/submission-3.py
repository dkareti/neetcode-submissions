class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """Evaluate the rpn expression."""
        digits = []
        
        for operand in tokens:
            if operand == "+":
                digits.append(digits.pop() + digits.pop())
            elif operand == "*":
                digits.append(digits.pop() * digits.pop())
            elif operand == "/":
                top, nxt = digits.pop(), digits.pop()
                digits.append(int(float(nxt) / top))
            elif operand == "-":
                top, nxt = digits.pop(), digits.pop()
                digits.append(nxt - top)
            else:
                digits.append(int(operand))
        
        return digits[0]
