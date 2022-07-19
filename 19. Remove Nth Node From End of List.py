"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def checklen(self, head):
        lent = 0
        cur_node = head
        while cur_node != None:
            lent += 1
            cur_node = cur_node.next
        return lent

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        llen = self.checklen(head)
        del_ind = llen - n
        result = []
        curNode = head
        if del_ind == 0:
            head = head.next
            return head
        while curNode != None:
            result.append(curNode)
            curNode = curNode.next
        for i in range(len(result)):
            if i == del_ind:
                if del_ind == llen - 1:
                    result[i - 1].next = None
                    break
                else:
                    result[i - 1].next = result[i + 1]
                    break
        return head
