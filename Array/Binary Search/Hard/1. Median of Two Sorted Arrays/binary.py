class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        import sys
        INT_MIN = -sys.maxsize
        INT_MAX = sys.maxsize

        while low <= high:
            Px = low + (high - low) // 2
            Py = (m + n + 1) // 2 - Px

            x1 = INT_MIN if Px == 0 else nums1[Px - 1]
            x3 = INT_MAX if Px == m else nums1[Px]


            x2 = INT_MIN if Py == 0 else nums2[Py - 1]
            x4 = INT_MAX if Py == n else nums2[Py]

            if x1 <= x4 and x2 <= x3:
                if (m + n) % 2 == 0:
                    return (max(x1, x2) + min(x3, x4)) / 2.0
                
                return max(x1, x2)
            
            elif x1 > 4:
                high = Px - 1
            else:
                low = Px + 1

        return -1
    
nums1 = [1,2]
nums2 = [3,4]
s = Solution().findMedianSortedArrays(nums1, nums2)
print(s)
