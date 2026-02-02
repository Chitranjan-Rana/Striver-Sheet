# 1011. Capacity To Ship Packages Within D Days

class Solution:
    def getDays(self, weights, capacity):

        days = 1
        currentLoad = 0

        for w in weights:
            if currentLoad + w > capacity:
                currentLoad = w
                days += 1

            else:
                currentLoad += w

        return days
    
    def shipWithinDays(self, weights, d):

        left = max(weights)
        right = sum(weights)

        for w in range(left, right + 1):
            needed = self.getDays(weights, w)
            if needed <= d:
                return w
            
        return right


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
s = Solution().shipWithinDays(weights, days)
print(s)