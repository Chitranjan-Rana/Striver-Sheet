class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [0] * n

        count_zero = nums.count(0)

        if count_zero > 1:
            return result
        
        
        if count_zero == 1:
            product_with_zero = 1

            for i in range(n):
                if nums[i] != 0:
                    product_with_zero *= nums[i]

            for i in range(n):
                if nums[i] == 0:
                    result[i] = product_with_zero

                else:
                    result[i] = 0

            return result

        else:

            product_all = 1

            for i in range(n):
                product_all *= nums[i]

            for i in range(n):
                result[i] = product_all // nums[i]

            return result
    
nums = [1,2,3,4]
s = Solution().productExceptSelf(nums)
print(s)

            
