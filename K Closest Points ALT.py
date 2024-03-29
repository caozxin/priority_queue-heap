#https://www.lintcode.com/problem/612/

from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
from heapq import heapify, heappop

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:

        if not k or not points:
            return []

        def distance(x, y, x_org, y_org):
            return (x-x_org)**2 + (y-y_org)**2 # note you do not use sqrt here, as using integer to represent the distance is more accurate

        x_org = origin.x
        y_org = origin.y
        heap = []
        for each in points:
            print(each.x, each.y)
            heap.append((distance(each.x, each.y, x_org, y_org), each))
        print("heap", heap) 
        # exit()
        # heap = [(distance(x, y), x, y) for x, y in points]
        # print("heap", heap) #[(10, 1, 3), (8, -2, 2)]
        heapify(heap)
        print("heap af", heap) # here the distance got heapified: [(8, -2, 2), (10, 1, 3)]

        res = []
        for _ in range(k):
            _, each_point = heappop(heap)
            res.append(each_point)

        return res
