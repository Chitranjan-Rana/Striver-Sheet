
# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutiveSequence(self, nums:list[int]) -> int:

        n = len(nums)
        longest = 0

        for i in range(n):
            current = nums[i]
            count = 1
             
            while current + 1 in nums:
                current += 1
                count += 1

            longest = max(longest, count)

        return longest
    

nums = [100,4,200,1,3,2]
s = Solution().longestConsecutiveSequence(nums)
print(s)