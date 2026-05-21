class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list(s)
        list2 = list(t)

        sum1 = 0
        sum2 = 0

        for i in list1:
            sum1 += ord(i)
        
        for j in list2:
            sum2 += ord(j)

        if(sum1 == sum2):
            return True
        else:
            return False