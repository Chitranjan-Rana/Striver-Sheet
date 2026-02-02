class Solution:
    def lowerBound(self, nums, x):
        
        n = len(nums)
        low = 0
        high = n - 1
        ans = n

        while low <= high:

            mid = (high + low ) // 2

            if nums[mid] >= x:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans
    
nums = [3,4,5,5,6,7,8]
x = 5
s = Solution().lowerBound(nums, x)
print(s)  # op => 2