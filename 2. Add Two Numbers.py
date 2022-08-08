"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode()
        curanswer = answer
        counter = 0
        curl1 = l1
        curl2 = l2
        while curl1 or curl2:
            if curl1 == None:
                sum = curl2.val + counter
            elif curl2 == None:
                sum = curl1.val + counter
            else:
                sum = curl1.val + curl2.val + counter
            if sum > 9:
                curanswer.val = sum - 10
                counter = 1
            else:
                curanswer.val = sum
                counter = 0
            if curl1 != None:
                curl1 = curl1.next
            if curl2 != None:
                curl2 = curl2.next
            if curl1 != None or curl2 != None:
                curanswer.next = ListNode()
                curanswer = curanswer.next
        if counter == 1:
            curanswer.next = ListNode()
            curanswer = curanswer.next
            curanswer.val = 1

        return answer
