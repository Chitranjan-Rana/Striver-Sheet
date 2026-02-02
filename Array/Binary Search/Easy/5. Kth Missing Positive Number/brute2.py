class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        n = len(arr)
        missingCount = 0
        num = 1
        i = 0

        while True:

            if i < n and arr[i] == num:
                i += 1

            else:
                missingCount += 1

                if missingCount == k:
                    return num
                
            num += 1

arr = [1,2,3,4]
k = 2
s = Solution().findKthPositive(arr, k)
print(s)