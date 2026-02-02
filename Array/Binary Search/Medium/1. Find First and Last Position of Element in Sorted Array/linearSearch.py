class Solution:
    def searchRange(self, nums: list[int], target: int) -> int:
        n = len(nums)
        first, last = -1, -1

        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]
    

nums = [5,6,7,7,8,8,9]
target = 8
s = Solution().searchRange(nums, target)
print(s)

