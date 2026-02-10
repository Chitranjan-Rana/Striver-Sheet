class Solution:
    def longestPalindrome2(self, s: str) -> str:

        n = len(s)

        t = [[False] * n for _ in range(n)]

        maxL = 1
        start = 0

        for i in range(n):
            t[i][i] = True

        for L in range(2, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1

                if s[i] == s[j] and (L == 2 or t[i + 1][j - 1]):
                    t[i][j] = True
                    if L > maxL:

                        maxL = L
                        start = i

        return s[start: start + maxL]
    
s = "cbbd"
sol = Solution().longestPalindrome2(s)
print(sol)