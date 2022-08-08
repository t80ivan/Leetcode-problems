"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


Constraints:

0 <= rowIndex <= 33
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex +=1
        result  = [[1]]
        if rowIndex>=2:
            result.append([1,1])
        counter = 3
        while counter<=rowIndex:
            row = [1]
            lp = 0
            rp = 1
            while rp<len(result[-1]):
                row.append(result[-1][lp] + result[-1][rp])
                lp+=1
                rp+=1
            row.append(1)
            result.append(row)
            counter+=1
        return result[-1]