class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Determine if two strings are anagrams of each other."""
        return collections.Counter(s) == collections.Counter(t)