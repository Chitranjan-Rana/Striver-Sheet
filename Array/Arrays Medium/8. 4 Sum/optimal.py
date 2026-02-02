class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        n = len(nums)
        ans = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1

                    elif total < target:
                        k += 1

                    else:
                        l -= 1

        return ans

nums = [2,2,2,2,2]
target = 8
s = Solution().fourSum(nums, target)
print(s)