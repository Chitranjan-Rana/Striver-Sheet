# hash table using in this approach

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        mpp = {}

        for i, num in enumerate(nums):
            moreNeeded = target - num

            if moreNeeded in mpp:
                return [mpp[moreNeeded], i]
            
            mpp[num] = i

        return [-1, -1]
    
nums = [2,6,8,4,7,9,5]
target = 14
s = Solution().twoSum(nums, target)
print(s)


# Time: O(n)
# Space: O(n)


