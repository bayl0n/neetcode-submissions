class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            
            new_stone = -abs(y - x)

            if new_stone != 0:
                heapq.heappush(max_heap, new_stone)

        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]