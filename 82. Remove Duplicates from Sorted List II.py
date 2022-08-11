"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        result = []
        values = {}
        while head != None:
            result.append(head)
            if values.get(head.val):
                values[head.val] += 1
            else:
                values[head.val] = 1
            head = head.next

        new_res = [i for i in result if values[i.val] == 1]
        if len(new_res) == 0:
            return None
        for i in range(len(new_res) - 1):
            new_res[i].next = new_res[i + 1]
        new_res[-1].next = None
        return new_res[0]
