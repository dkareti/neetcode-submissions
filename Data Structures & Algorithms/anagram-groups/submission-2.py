class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group all similar anagrams together."""
        seen = collections.defaultdict(list)

        for item in strs:
            seen["".join(sorted(item))].append(item)
        
        return list(seen.values())