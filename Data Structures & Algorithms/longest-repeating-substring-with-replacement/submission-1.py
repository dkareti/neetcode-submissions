class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Find the longest string that can be formed using character replacements."""
        longest = 0
        seen = collections.defaultdict(int)
        max_freq = 0
        left = 0

        for right, char in enumerate(s):
            seen[char] += 1
            max_freq = max(max_freq, seen[char])

            while (right - left + 1) - max_freq > k:
                seen[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest