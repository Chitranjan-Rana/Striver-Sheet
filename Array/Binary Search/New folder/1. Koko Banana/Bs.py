import math
class solution:
    def minEatingBanana(self, piles: list[int], h: int) -> int:

        low = 1
        high = max(piles)
        result = high

        while low <= high:
            mid = (low + high) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/mid)

            if total_hours <= h:
                result = mid
                high = mid - 1

            else:
                low = mid + 1

        return result
    
piles = [30,11,23,4,20]
h = 5
s = solution().minEatingBanana(piles, h)
print(s)
