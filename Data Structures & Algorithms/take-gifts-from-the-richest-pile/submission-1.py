class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        while k > 0:
            maxValue = -(heapq.heappop(max_heap))
            heapq.heappush(max_heap, int(-sqrt(maxValue)))
            k -= 1
        
        return -sum(max_heap)