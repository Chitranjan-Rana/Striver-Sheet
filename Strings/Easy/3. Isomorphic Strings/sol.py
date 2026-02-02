# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mp1 = {}
        mp2 = {}

        for i in range(len(s)):
           ch1 = s[i]
           ch2 = t[i]

           if (ch1 in mp1 and mp1[ch1] != ch2) or (ch2 in mp2 and mp2[ch2] != ch1):
               return False

        return True
    
s = "egg" 
t = "add"
sol = Solution().isIsomorphic(s, t)
print(sol)