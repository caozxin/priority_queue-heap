"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

import heapq
from heapq import heappop, heappush

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        res = ListNode(None)

        def searchListNode(alist: ListNode, heap):

            if not alist:
                return

            # print(alist.val)
            heappush(heap, alist.val)
            # print("heap", heap)

            if alist.next:
                # temp = alist.next
                # alist.val = temp
                searchListNode(alist.next, heap)

        for each_list in lists:
            searchListNode(each_list, heap)

        # heap.sort()

        # print("heap", heap)

        # Initialize the dummy node
        dummy = ListNode(None)
        current = dummy

        while heap:
            curr_node = heapq.heappop(heap)
            # print("curr_node:", curr_node)
            current.next = ListNode(curr_node)
            current = current.next

        return dummy.next

        # return res

