# 75 sort colors


class Solution:
    def sortColors(self, nums:list[int]) -> int:

        n = len(nums)
        count0, count1, count2 = 0, 0, 0

        for i in range(n):
            if nums[i] == 0:
                count0 += 1

            elif nums[i] == 1:
                count1 += 1

            else:
                count2 += 1

        
        idx = 0

        for i in range(count0):
            nums[idx] = 0
            idx += 1
        
        for i in range(count1):
            nums[idx] = 1
            idx += 1
        
        for i in range(count2):
            nums[idx] = 2
            idx += 1

        return nums

nums = [2,1,2,1,2,1,0,2,0,0,1,0]
s = Solution().sortColors(nums)
print(s)

        