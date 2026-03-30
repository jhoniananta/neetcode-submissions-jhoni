from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for x in stones:
            heapq.heappush(max_heap, -x)
        
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if y > x:
                heapq.heappush(max_heap, x - y)
        
        max_heap.append(0)
        return abs(max_heap[0])