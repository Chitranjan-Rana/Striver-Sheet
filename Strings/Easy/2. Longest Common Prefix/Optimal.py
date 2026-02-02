class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""
        
        strs.sort()

        first = strs[0]
        last = strs[-1]
        result = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])

        return "".join(result)
    
strs = ["flower","flow","floght"]
sol = Solution().longestCommonPrefix(strs)
print('Longest common prefix:',sol)