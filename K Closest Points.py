from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k or not points:
            return []

        def distance(x, y):
            return x**2 + y**2

        heap = [(distance(x, y), x, y) for x, y in points]
        print("heap", heap) #[(10, 1, 3), (8, -2, 2)]
        heapify(heap)
        print("heap af", heap) # here the distance got heapified: [(8, -2, 2), (10, 1, 3)]

        res = []
        for _ in range(k):
            _, x, y = heappop(heap)
            res.append([x, y])

        return res
