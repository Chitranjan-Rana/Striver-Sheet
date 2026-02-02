class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        n = len(nums)
        start = 0
        end = n - 1

        if n == 1:
            return nums[0]
        
        while start <= end:
            mid = start + (end - start) // 2

            # if mid is in index 0
            if mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            # if mid is in last index
            elif mid == n - 1 and nums[n - 1] != nums[n - 2]:
                return nums[mid]
            
            elif nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # if mid is even 

            elif mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:   # check in same direction
                    end = mid - 1
                else:
                    start = end + 1

            else:
                if nums[mid] == nums[mid - 1]:  # check in opposite direction
                    start = end + 1

                else:
                    end = mid - 1

        return -1
    
nums = [1,1,2,2,3,4,4,5,5]  # output - 3
s = Solution().singleNonDuplicate(nums)
print(s)
