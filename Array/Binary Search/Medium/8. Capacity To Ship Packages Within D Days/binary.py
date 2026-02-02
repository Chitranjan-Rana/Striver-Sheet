class Solution:
    def daysNeeded(self, weights, capacity):

        days = 1
        currentLoad = 0

        for w in weights:
            if currentLoad + w > capacity:               
                days += 1
                currentLoad = w

            else:
                currentLoad += w

        return days
    
    def shipWithinDays(self, weights, d):

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            needed = self.daysNeeded(weights, mid)

            if needed <= d:
                right = mid

            else:
                left = mid + 1

        return left
    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
s = Solution().shipWithinDays(weights, days)
print(s)