# using 2 pointer 
# 189. Rotate Array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)
        k %= n  # To handle k > n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n-1)  # Step 1: Reverse entire array
        reverse(0, k-1)  # Step 2: Reverse first k elements
        reverse(k, n-1)  # Step 3: Reverse rest


nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)



