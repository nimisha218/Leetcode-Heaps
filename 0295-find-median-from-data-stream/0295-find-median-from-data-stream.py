class MedianFinder:
    # 3.27pm 
    def __init__(self):
        self.smallHeap = []
        heapq.heapify(self.smallHeap)
        self.largeHeap = []
        heapq.heapify(self.largeHeap)
        
    def addNum(self, num: int) -> None:

        if len(self.smallHeap) == 0 and len(self.largeHeap) == 0:
            heapq.heappush(self.smallHeap, -num)
            
        else:
            if len(self.smallHeap) > 0:
                current = heapq.heappop(self.smallHeap)
                heapq.heappush(self.smallHeap, current)
                if num <= -current:
                    heapq.heappush(self.smallHeap, -num)
                else:
                    heapq.heappush(self.largeHeap, num)
                
        if (len(self.smallHeap) - len(self.largeHeap)) >= 2:
            max_num = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -max_num)
        if (len(self.largeHeap) - len(self.smallHeap)) >= 2:
            min_num = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -min_num)

    def findMedian(self) -> float:
        
        # Even number of elements
        if len(self.smallHeap) == len(self.largeHeap):
            left = heapq.heappop(self.smallHeap)
            heapq.heappush(self.smallHeap, left)
            right = heapq.heappop(self.largeHeap)
            heapq.heappush(self.largeHeap, right)
            return (-left + right) / 2
        # Odd number of elements
        else:
            if len(self.smallHeap) > len(self.largeHeap):
                res = heapq.heappop(self.smallHeap)
                heapq.heappush(self.smallHeap, res)
                return -res
            else:
                res = heapq.heappop(self.largeHeap)
                heapq.heappush(self.largeHeap, res)
                return res

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()