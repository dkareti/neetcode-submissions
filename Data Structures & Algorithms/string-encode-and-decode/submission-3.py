class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for item in strs:
            ans += str(len(item))
            ans += "#"
            ans += item
        
        return ans

    def decode(self, s: str) -> List[str]:
        
        res = []
        left = 0
        
        while left <= len(s) - 1:
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right]) # slicing is right exclusive
            left = right + 1 # placing the pointer after the length and #
            right = left + length
            res.append(s[left:right]) # adding the string to the list
            left = right

        return res

            
