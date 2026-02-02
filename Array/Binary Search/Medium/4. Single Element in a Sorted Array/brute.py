
# 540. Single Element in a Sorted Array (Brute)

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        
        for i in range(n):

            if i == 0:
                if nums[i] != nums[i + 1]:  # check right side of element
                    return nums[i]
                
            elif i == n - 1:
                if nums[i] != nums[i - 1]:  # check left side of element
                    return nums[i]
                
            else:
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]
                

        return nums[-1]
    
nums = [1,1,2,2,3,3,4,5,5,6,6]
s = Solution().singleNonDuplicate(nums)
print(s)