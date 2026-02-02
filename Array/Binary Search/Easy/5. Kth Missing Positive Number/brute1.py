# 1539. Kth Missing Positive Number

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        for num in arr:
            if num <= k:
                k += 1

            else:
                break

        return k
    
arr = [2,3,4,7,11]
k = 5
s = Solution().findKthPositive(arr, k)
print(s)