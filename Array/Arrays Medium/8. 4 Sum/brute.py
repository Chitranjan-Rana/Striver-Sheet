# 18. 4Sum
# Do not submit because it gives time exeeced error

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        val = nums[i] + nums[j] + nums[k] + nums[l]

                        if val == target:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))


        return [list(x) for x in ans]
    
nums = [1,0,-1,0,-2,2]
target = 0
s = Solution().fourSum(nums, target)
print(s)