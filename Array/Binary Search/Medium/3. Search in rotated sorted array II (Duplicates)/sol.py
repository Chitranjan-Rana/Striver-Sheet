# 81. Search in Rotated Sorted Array II

class Solution:
    def search(self, nums:list[int], target: int) -> bool:

        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True
            
            # if same no. in start, mid and end

            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                start += 1
                end -= 1
                continue

            # left search

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

        return False
    
nums = [2,5,6,0,0,1,2]
target = 0
s = Solution().search(nums, target)
print(s)

