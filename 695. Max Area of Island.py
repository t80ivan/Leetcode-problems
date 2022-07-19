"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""


class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1:
            if len(grid[0]) == 1:
                return grid[0][0]
        R, C = len(grid), len(grid[0])
        visited = []
        point = []
        result = []

        def dfs(r, c):
            if [r, c] not in visited:
                if grid[r][c] == 1:
                    visited.append([r, c])
                    point.append([r, c])
                    if r >= 1:
                        dfs(r - 1, c)
                    if r + 1 < R:
                        dfs(r + 1, c)
                    if c >= 1:
                        dfs(r, c - 1)
                    if c + 1 < C:
                        dfs(r, c + 1)

        for i in range(len(grid)):
            point = []
            for s in range(len(grid[0])):
                if grid[i][s] == 0:
                    if len(point) not in result:
                        result.append(len(point))
                    point = []
                else:
                    dfs(i, s)
                    if len(point) not in result:
                        result.append(len(point))
                    point = []
        if len(point) not in result:
            result.append(len(point))
        return max(result)
