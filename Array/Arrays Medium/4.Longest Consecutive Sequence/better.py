class Solution:
    def longestConsecutiveSequence(self, nums:list[int]) -> int:

        n = len(nums)
        lastSmaller = float('inf')
        count = 0
        longest = 1
        nums.sort()
    

        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                count += 1
                lastSmaller = nums[i]

            elif lastSmaller != nums[i]:
                count = 1
                lastSmaller = nums[i]

            longest = max(longest, count)

        return longest
    

nums = [100,4,200,1,3,2]
s = Solution().longestConsecutiveSequence(nums)
print(s)
        
            
