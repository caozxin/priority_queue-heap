#Merge k sorted chains (sequences are ascending sequences) and return the merged sorted chains (sequences are ascending sequences). Try to analyse and describe its complexity.

#Analyze and describe its complexity
"""
Given k sorted lists of numbers, merge them into one sorted list.

Input: [[1, 3, 5], [2, 4, 6], [7, 10]]

Output: [1, 2, 3, 4, 5, 6, 7, 10]
"""
import heapq

# Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

"""


from typing import List
from heapq import heappop, heappush
def merge_k_sorted_lists_def(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    # def compare_each_list(list)
    print("result: ", lists)
    #None handling:
    if not lists:
        return []

    res = []
    heap = []
    for current_list in lists:
        # push first number of each list into the heap
        heappush(heap, (current_list[0], current_list, 0)) # 1

    while heap:
        val, current_list, head_index = heappop(heap)
        res.append(val)
        head_index += 1
        # if there are more numbers in the list, push into the heap
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))

    print("res", res)
    return res
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    # def compare_each_list(list)
    print("result: ", lists)
    #None handling:
    if not lists:
        return []

    res = []
    heap = []
    n = len(lists)

    for current_list in lists:
        # push first number of each list into the heap
        heappush(heap, (heappop(current_list), current_list, 0))  # 1
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
    exit()

    while heap:
        curr_node = heappop(heap)
        print(curr_node, heap)

        for each_list in lists:
            compare_node = heappop(each_list)
            print(curr_node, compare_node)
            if compare_node:
                exit()



input = [[1, 3, 5], [2, 4, 6], [7, 10]]
merge_k_sorted_lists(input)