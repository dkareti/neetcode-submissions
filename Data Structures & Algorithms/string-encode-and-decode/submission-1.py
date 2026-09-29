class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encode the list of strs."""
        if not strs:
            return ""
        result = ""
        for item in strs:
            result += str(len(item))
            result += "#"
            result += item
        return result

    def decode(self, s: str) -> List[str]:
        """Decode the string s."""
        left = 0 #store a pointer that traverses through the string
        ans = []
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            
            number = int(s[left:right])
            
            #find the word
            start = right + 1
            value = s[start: start + number]
            ans.append(value)

            #increment the left pointer
            left = start + number
        return ans



