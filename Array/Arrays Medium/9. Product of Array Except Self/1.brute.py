# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result
    
nums = [1,2,3,4]
s = Solution().productExceptSelf(nums)
print(s)