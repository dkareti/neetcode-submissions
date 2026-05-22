class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Find if the string s is a valid palindrome or not."""
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].isalnum():
                left += 1
                continue

            if s[right].lower() != s[left].lower():
                return False
            
            left += 1
            right -= 1

        return True