# 5. Longest Palindromic Substring

class Solution:
    def solve(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
    
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        maxLen = float('-inf')
        startingIndex = 0

        for i in range(n):
            for j in range(i, n):
                if self.solve(s, i, j):
                    if j - i + 1 > maxLen:
                        startingIndex = i
                        maxLen = j - i + 1

        return s[startingIndex: startingIndex + maxLen]
    

s = "cbbd"
sol = Solution().longestPalindrome(s)
print(sol)