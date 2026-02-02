# using dutch flag algorithm---

class Solution:
    def sortColors2(self, nums:list[int]) -> int:

        n = len(nums)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1

        return nums
    
nums = [2,2,1,2,1,0,0,1,0]
s = Solution().sortColors2(nums)
print(s)

# time - O(n)
# space - O(1)
            