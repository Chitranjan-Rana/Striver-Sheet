# 33. Search in Rotated Sorted Array(Binary Search)


class Solution:
    def search(self, nums:list[int], target: int) -> int:

        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1

                else:
                    start = mid + 1

            else:

                if nums[mid] <= target <= nums[end]:
                    start = mid + 1

                else:
                    end = mid - 1

        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0
s = Solution().search(nums, target)
print(s)
