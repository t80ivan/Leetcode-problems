"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ = 0
        pows = 1
        for i in str(n):
            summ += int(i)
            pows *= int(i)
        return pows - summ
