from typing import List
from collections import deque

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def merge_two_interval_testing(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
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


    

    def merge_two_interval_def(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]:
        if not list1 and not list2: # None handling, return the null of expected result format
            return []

        merged_intervals = []
        list1_queue = deque(list1)
        list2_queue = deque(list2)

        while list1_queue and list2_queue:
            interval1 = list1_queue.popleft()
            interval2 = list2_queue.popleft()

            if interval1.end < interval2.start:
                merged_intervals.append(interval1)
                list2_queue.appendleft(interval2)
            elif interval2.end < interval1.start:
                merged_intervals.append(interval2)
                list1_queue.appendleft(interval1)
            else:
                new_start = min(interval1.start, interval2.start)
                new_end = max(interval1.end, interval2.end)
                merged_intervals.append(Interval(new_start, new_end))

        # Add remaining intervals from list1_queue and list2_queue if any
        merged_intervals.extend(list1_queue)
        merged_intervals.extend(list2_queue)

        return merged_intervals


    def merge_two_interval(self, list1, list2):
        # write your code here
        res = []
        index1, index2, size1, size2 = 0, 0, len(list1), len(list2)
        while index1 < size1 or index2 < size2:
            if index1 == size1:
                self.merge(res, list2[index2])
                index2 += 1 
            elif index2 == size2:
                self.merge(res, list1[index1])
                index1 += 1 
            elif list1[index1].start < list2[index2].start:
                self.merge(res, list1[index1])
                index1 += 1 
            else:
                self.merge(res, list2[index2])
                index2 += 1 
        return res    
        
    def merge(self, res, interval):
        if not res:
            res.append(interval)
        elif res[-1].end >= interval.start:
            res[-1].end = max(res[-1].end, interval.end)
        else:
            res.append(interval)



    def print_res(self, res):

        if len(res) > 0:
            for each in res:
                print(" print_res:", each.start, each.end)

    def merge(self, res, interval):
        if not res:
            res.append(interval)
        elif res[-1].end >= interval.start: # last Interval in res, this check for overlapping. 
            res[-1].end = max(res[-1].end, interval.end)
        else:
            res.append(interval)

    def merge_two_interval_attempt(self, list1: List[Interval], list2: List[Interval]) -> List[Interval]: # this needs to be updated. 
        # write your code here

        if not list1 and not list2: # None handling, return the null of expected result format
            return []

        res = []
        list1_queue = deque(list1)
        list2_queue = deque(list2)

        while len(list1_queue) > 0 or len(list2_queue)>0:

            if len(list1_queue) > 0 and len(list2_queue)>0:
                interval1 = list1_queue.popleft()
                interval2 = list2_queue.popleft()
                
                if interval1.end <= interval2.start: # this also check if interval1 and interval2 have overlap
                    self.merge(res, interval1)
                    print("res1", self.print_res(res))
                    # exit()
                    self.merge(res, interval2)
                    print("res2", self.print_res(res))
                # exit()
            if len(list1_queue) > 0 and len(list2_queue) == 0:
                interval1 = list1_queue.popleft()
                self.merge(res, interval1)
                # exit()

            if len(list2_queue) > 0 and len(list1_queue) == 0:
                interval2 = list2_queue.popleft()
                self.merge(res, interval2)
            
        return res
    






