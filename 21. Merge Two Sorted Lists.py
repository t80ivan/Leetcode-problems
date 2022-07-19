"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        nodeslist = []
        curl1 = l1
        curl2 = l2
        while curl1 is not None:
            nodeslist.append(curl1)
            curl1 = curl1.next
        while curl2 is not None:
            nodeslist.append(curl2)
            curl2 = curl2.next
        nodeslist.sort(key=lambda x: x.val, reverse=False)
        for i in range(len(nodeslist) - 1):
            nodeslist[i].next = nodeslist[i + 1]
        return nodeslist[0]
