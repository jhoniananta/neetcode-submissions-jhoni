class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1

        res = 0

        while left <= right:
            capacity = limit - people[right]
            res += 1
            right -= 1

            if people[left] <= capacity:
                left += 1
        
        return res
