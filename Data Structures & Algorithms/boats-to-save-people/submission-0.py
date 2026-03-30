class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) -1

        counter = 0

        while left <= right:
            remain = limit - people[right]
            right -= 1
            counter += 1

            if remain >= people[left] and left <= right:
                left += 1
        
        return counter