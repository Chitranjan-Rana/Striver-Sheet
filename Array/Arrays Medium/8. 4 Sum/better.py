class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    fourth = target - nums[i] - nums[j] - nums[k]

                    if fourth in seen:
                        quad = sorted([nums[i], nums[j], nums[k], fourth])
                        result.add(tuple(quad))

                    seen.add(nums[k])

        return [list(quad) for quad in result]
    
nums = [1,0,-1,0,-2,2]
target = 0
s = Solution().fourSum(nums, target)
print(s)