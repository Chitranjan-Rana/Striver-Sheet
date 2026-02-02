# 1. Two Sum

class Solution:
    def findTwoSum(self, nums:list[int], target:int) -> list[int]:

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []
    

nums = [2,5,6,8,4,7,9,5]
target = 14
s = Solution().findTwoSum(nums, target)
print(s)


# Time: O(n²) — two nested loops

# Space: O(1) — no extra space used