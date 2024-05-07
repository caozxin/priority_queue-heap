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
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    # def compare_each_list(list)
    print("result: ", lists)
    #None handling:
    if not lists:
        return []

    new_list = []
    for each_sublist in lists:
        print(each_sublist)
        # each_sublist = heapq.heapify(each_sublist)
        # each_sublist = heapq.heapify(each_sublist)

        while len(each_sublist) > 0:

            if len(new_list) == 0:
                curr_node = heappop(each_sublist) # you need to pop the first one
                new_list.append(curr_node)
                print(new_list)
            else:
                curr_node = heappop(new_list)
                compare_node = heappop(each_sublist)
                print(curr_node, compare_node)
                exit()
                if curr_node < compare_node:
                    new_list.append(curr_node)
                    heappush(compare_node)
                # else:




input = [[1, 3, 5], [2, 4, 6], [7, 10]]
merge_k_sorted_lists(input)