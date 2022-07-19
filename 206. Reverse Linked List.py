"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        result = deque()
        cur_node = head
        while cur_node != None:
            result.appendleft(cur_node)
            cur_node = cur_node.next
            if len(result) == 1:
                result[-1].next = None
            else:
                result[0].next = result[1]
        return result[0]
