class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def first_occurrence(arr: list[int], k: int) -> int:
            low, high = 0, len(arr) - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    first = mid
                    high = mid - 1   # keep searching left
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def last_occurrence(arr: list[int], k: int) -> int:
            low, high = 0, len(arr) - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    last = mid
                    low = mid + 1   # keep searching right
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [first_occurrence(nums, target), last_occurrence(nums, target)]
    

# Test
nums = [3,4,5,6,6,6,7]
target = 6
s = Solution().searchRange(nums, target)
print(s)

        

