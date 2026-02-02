class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        s.reverse()

        n = len(s)
        i, l, = 0, 0
        res = []

        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break

            word = []
            while i < n and s[i] != ' ':
                word.append(s[i])
                i += 1
            res.append("".join(reversed(word)))

        return " ".join(res)
    
s = " i am a boy "
sol = Solution().reverseWords(s)
print(sol)

