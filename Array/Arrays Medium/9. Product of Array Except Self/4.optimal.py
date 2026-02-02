class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * right_product
            right_product *= nums[i]

        return result

nums = [1,2,3,4]
s = Solution().productExceptSelf(nums)
print(s)