# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""
        
        first = strs[0]
        ans = ""

        for i in range(1, len(strs) + 1):
            prefix = first[:i]

            for word in strs:
                if not word.startswith(prefix):
                    return ans
                
            ans  = prefix

        return ans
    
strs = ["flower","flow","flight"]
sol = Solution().longestCommonPrefix(strs)
print('Longest common prefix:',sol)