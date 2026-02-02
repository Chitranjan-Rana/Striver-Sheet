class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [0] * n
        left   = [0] * n
        right  = [0] * n

        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        for i in range(n- 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(n):
            result[i] = left[i] * right[i]

        return result

nums = [1,2,3,4]
s = Solution().productExceptSelf(nums)
print(s)