class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        def isPossible(bloom_days, m, day, k):
            count = 0
            bouquets = 0

            for bloom in bloom_days:
                if bloom <= day:
                    count += 1     
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            return bouquets >= m

        def bruteForce(bloom_days, m, k):

            totalFlowers = m * k
            if totalFlowers > len(bloom_days):
                return -1
            
            low = min(bloom_days)
            high = max(bloom_days)

            for day in range(low, high + 1):
                if isPossible(bloom_days, m, day, k):   
                    return day

            return -1

        return bruteForce(bloomDay, m, k)


bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(Solution().minDays(bloomDay, m, k))
