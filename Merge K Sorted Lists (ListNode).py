"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import heappop, heappush


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here

        print("result: ", lists)
        # None handling:
        if not lists:
            return []

        res = []
        heap = []
        n = len(lists)

        for curr_list in lists:
            # push first number of each list into the heap
            print("curr_list", curr_list)
            exit()
            curr_heap = [heappop(curr_list), curr_list, 0]
            print(curr_heap)
            exit()
            # heappush(heap, (heappop(current_list), current_list, 0))  # 1

        exit()
        while heap:
            print("remaining lists: ", lists)
            print("heap", heap)
            curr_node = heappop(heap)
            # print(curr_node)
            res.append((curr_node[0]))
            print(res)
            if curr_node[1]:
                current_list = curr_node[1]
                # print(current_list)
                # exit()
                heappush(heap, (heappop(current_list), current_list, 0))
                print("after", heap)
        return res