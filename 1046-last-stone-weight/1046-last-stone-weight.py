import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            x = - heapq.heappop(maxHeap)
            y = - heapq.heappop(maxHeap)
        
            if x != y:
                heapq.heappush(maxHeap, y-x)

        return -maxHeap[0] if maxHeap else 0

        