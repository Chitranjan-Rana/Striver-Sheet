# 744. Find Smallest Letter Greater Than Target

class Solution:
    def findSmallLetter(self, letters: list[str], target: str) -> str:
        
        n = len(letters)
        start, end = 0, n - 1
        ans = letters[0]

        while start <= end:
            mid = start + (end - start) // 2

            if letters[mid] > target:
                ans = letters[mid]
                end = mid - 1

            else:
                start = mid + 1

        return ans
    
s = Solution().findSmallLetter(letters=['a','b','d','g','j','k'], target='i') 
print(s)

# output - 'j'


