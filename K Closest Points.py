#Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k or not points:
            return None

        def distance(x, y):
            return sqrt(x**2 + y**2)

        n = len(points)
        print(n)

        dis_dict = {}
        heap = []
        for each in points:
            each_distance = distance(each[0], each[1])
            heap.append(each_distance)
            dis_dict[(each[0], each[1])] = each_distance
            # dis_dict[each_distance] = each
        print(dis_dict)
        
        heapify(heap)
        print(heap)
        res = set()

        for i in range(k):
            valu_dist = heappop(heap)
            for key, value in dis_dict.items():
                if value == valu_dist:
                    res.add(key)
            
        print(res)

        return res
