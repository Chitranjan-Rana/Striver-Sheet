# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1

            else:
                merged.append(nums2[j])
                j += 1

        merged += nums1[i:]
        merged += nums2[j:]

        # find median
        n = len(merged)

        if n % 2 == 1:
            return merged[n // 2]
        
        else:
            return (merged[n // 2] + merged[n // 2 - 1]) / 2.0
        
    
nums1 = [1,2]
nums2 = [3,4]
s = Solution().findMedianSortedArrays(nums1, nums2)
print(s)