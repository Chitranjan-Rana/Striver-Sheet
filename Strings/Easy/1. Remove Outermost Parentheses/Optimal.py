# 1021. Remove Outermost Parentheses

class Solution:
    def outermostPar(self, s: str) -> str:

        count = 0
        ans = []

        for i in range(len(s)):
            if s[i] == "(":
                count += 1
                if count > 0:
                    ans.append(s[i])
            elif s[i] == ")":
                count -= 1
                if count > 0:
                    ans.append(s[i])

        return "".join(s[ans])
