class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return - 1
    

nums = [2,4,5,8,9,5]
target = 9
s = Solution().search(nums, target)
print(s)