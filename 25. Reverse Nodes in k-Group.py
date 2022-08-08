"""
25. Reverse Nodes in k-Group
Hard

8412

521

Add to List

Share
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        node_list = []
        cur_node = head
        while cur_node != None:
            counter = k
            templist = []
            while counter > 0:
                templist.append(cur_node)
                cur_node = cur_node.next
                counter -= 1
                if cur_node == None:
                    counter = 0
            if len(templist) == k:
                for i in templist[::-1]:
                    node_list.append(i)
            else:
                for i in templist:
                    node_list.append(i)
        for i in range(len(node_list)):
            if i < len(node_list) - 1:
                node_list[i].next = node_list[i + 1]
            else:
                node_list[i].next = None
        return node_list[0]