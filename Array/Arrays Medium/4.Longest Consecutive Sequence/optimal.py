class Solution:
    def longestConsecutiveSequence3(self, nums:list[int]) -> int:

        n = len(nums)
        longest = 1
        st = set(nums)

        for num in st:
            if num - 1 not in st:
                count = 1
                x = num

                while x + 1 in st:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest
    

nums = [100,4,200,1,3,2]
s = Solution().longestConsecutiveSequence3(nums)
print(s)
        