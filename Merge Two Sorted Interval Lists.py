from typing import (
    List,
)
from lintcode import (
    Interval,
)

from heapq import heapify, heappop, heappush
from collections import deque

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def merge_two_interval(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        # write your code here

        if not list1 and not list2: # None handling, return the null of expected result format
            return []

        res = []
        list1 = deque(list1)
        list2 = deque(list2)

        def merge(interval1:Interval , interval2: Interval) -> List[Interval]:
            #note: when dealing with intervals, they should be pre-sorted. And it is already true for this case

            if interval1.end >= interval2.start:
                interval1.end = interval2.end
                print("af merg: ", interval1.start, interval1.end)
                return [interval1]
            print("no merg")
            return [interval1, interval2]

        if not res:
            curr_intv = list1.popleft()
            compare_intv = list2.popleft()
            res = merge(curr_intv, compare_intv)

        #when res not null:
        
        while len(list1) > 0:
            curr_intv = res.pop()
            compare_intv = list1.popleft()
            # print(curr_intv.start, compare_intv.start)
            res = merge(curr_intv, compare_intv)
            # res = res + merge(curr_intv, compare_intv)
            # print(res[0].start,res[0].end)
            # print(len(res), res)
            # exit()
            while len(list2) > 0:
                curr_intv = res.pop()
                compare_intv = list2.popleft()
                res = merge(curr_intv, compare_intv)
                # print(res[0].start,res[0].end)
                # print(len(res), res)
        return res


    






