class Solution:
    def isValid(self, s: str) -> bool:
        """Determine if a string has a valid set of parenthesis."""

        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char not in mapping:
                stack.append(char)
            elif char in mapping and not stack:
                return False
            elif stack: 
                value = stack.pop()
                if mapping[char] != value:
                    return False
        
        return len(stack) == 0