class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group the anagrams together."""
        seen = {}

        for word in strs:
            common = "".join(sorted(word))
            if common not in seen:
                seen[common] = []
            seen[common].append(word)

        return list(seen.values())