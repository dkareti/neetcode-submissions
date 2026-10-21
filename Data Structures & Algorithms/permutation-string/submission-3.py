class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Find if a permutation of s1 is a subset of s2."""
        if len(s1) > len(s2):
            return False
        
        #perform 1st iteration of sliding window
        counts_s1, counts_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            counts_s1[ord(s1[i]) - ord('a')] += 1
            counts_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if counts_s1[i] == counts_s2[i] else 0)

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            #Move the beginning of the string
            index = ord(s2[left]) - ord('a')
            counts_s2[index] -= 1
            if counts_s1[index] == counts_s2[index]:
                matches += 1
            elif counts_s1[index] - 1 == counts_s2[index]:
                matches -= 1

            #Move the end of the string
            index = ord(s2[right]) - ord('a')
            counts_s2[index] += 1
            if counts_s1[index] == counts_s2[index]:
                matches += 1
            elif counts_s1[index] + 1 == counts_s2[index]:
                matches -= 1
            left += 1
        return matches == 26