# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:

        openBrackets = 0
        result = 0

        for ch in s:
            if ch == '(':
                openBrackets += 1

            elif ch == ')':
                openBrackets -= 1

            result = max(result, openBrackets)

        return result
    
s = "(1+(2*3)+((8)/4))+1"
sol = Solution().maxDepth(s)
print(sol)