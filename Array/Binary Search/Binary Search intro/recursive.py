class Solution:
    def bs(self, nums: list[int], low: int, high: int, target: int) -> int:

        if low > high:
            return - 1
        
        mid = (high + low) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return self.bs(nums, mid + 1, high, target)
        
        else:
            return self.bs(nums, high - 1, low, target)
        
    
    def search(self, nums:list[int], target: int) -> int:
        return self.bs(nums, 0, len(nums) - 1, target)
        

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))   # Output: 4
print(sol.search([-1,0,3,5,9,12], 2))   # Output: -1


