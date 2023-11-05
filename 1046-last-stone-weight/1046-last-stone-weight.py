class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]
    
        self.minHeap = stones
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > 1:
            first = -heapq.heappop(self.minHeap)
            second = -heapq.heappop(self.minHeap)
            if first == second:
                continue
            else:
                if first <= second:
                    second = second - first
                    heapq.heappush(self.minHeap, -second)
                else:
                    first = first - second
                    heapq.heappush(self.minHeap, -first)
        
        if len(self.minHeap) == 1:
            return -self.minHeap[0]
        else:
            return 0

