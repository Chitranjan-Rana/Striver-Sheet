class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:

        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            missing = arr[mid] - (mid + 1) # Number of missing numbers before index mid

            if missing < k:
                low = mid + 1  # Need more missing values, go right
            else:
                high = mid - 1 # Too many missing, go left

        return k + high + 1
    
arr = [1,2,3,4]
k = 2
s = Solution().findKthPositive(arr, k)
print(s)

            