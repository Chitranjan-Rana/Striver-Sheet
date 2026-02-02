# 151. Reverse Words in a String

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"



class Solution:
    def reverseWords(self, s: str) -> str:

        result = ""

        for token in s.split():
            result = token + " " + result

        return result.strip()
    
s = " i am a boy "
sol = Solution().reverseWords(s)
print(sol)