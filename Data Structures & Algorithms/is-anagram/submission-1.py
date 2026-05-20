class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = "".join(s1)

        t1 = sorted(t)
        t2 = "".join(t1)

        if(t2 == s2):
            return True
        else:
            return False