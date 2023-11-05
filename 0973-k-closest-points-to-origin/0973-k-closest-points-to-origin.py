class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Phase 1:
        # Create a dictionary with keys as the distances from the point to the 
        # origin and values as a tuple representing that point

        distances = {}
        self.minHeap = []

        for point in points:

            x1, y1 = point[0], point[1]
            x2 = 0
            y2 = 0
            
            distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
            self.minHeap.append(distance)

            if distance not in distances:
                distances[distance] = [(x1, y1)]
            else:
                distances[distance].append((x1, y1))

        heapq.heapify(self.minHeap)
        
        result = []

        while True:
            res = heapq.heappop(self.minHeap)
            for point in distances[res]:
                result.append(point)
                if len(result) == k:
                    return result