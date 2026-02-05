# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:

        vec = [['', 0] for _ in range(123)]

        for ch in s:
            freq = vec[ord(ch)][1]
            vec[ord(ch)] = [ch, freq + 1]

        vec.sort(key=lambda p:p[1], reverse=True)

        result = ""
        for i in range(123):
            result += vec[i][0] * vec[i][1]

        return result
    
s = "tree"
s = Solution().frequencySort(s)
print(s)