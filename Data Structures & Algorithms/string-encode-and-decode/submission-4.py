class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for string in strs:
            ans += str(len(string))
            ans += "#"
            ans +=  string

        return ans

    def decode(self, s: str) -> List[str]:
        left = 0
        ans = []
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            strLength = int(s[left:right])
            left = right + 1
            right = left + strLength
            ans.append(s[left:right])

            #assign the left pointer to a new value
            left = right
        return ans
