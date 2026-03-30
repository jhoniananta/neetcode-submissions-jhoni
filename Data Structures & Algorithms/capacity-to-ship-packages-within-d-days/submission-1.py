
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def canShip(capacity: int):
            days_used = 1
            current_load = 0

            for w in weights:
                if current_load + w <= capacity:
                    current_load += w
                else:
                    days_used += 1
                    current_load = w
            return days_used <= days

        while l < r:
            mid = l + (r-l) // 2

            if canShip(mid):
                r = mid
            else:
                l = mid + 1
        
        return l