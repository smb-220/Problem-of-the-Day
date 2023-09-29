import sys
from typing import List
sys.setrecursionlimit(10**8)

def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return
    
    grid[i][j] = 0
    dfs(i + 1, j, grid)
    dfs(i, j + 1, grid)
    dfs(i, j - 1, grid)
    dfs(i - 1, j, grid)

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1 and grid[i][j] == 1:
                    dfs(i, j, grid)
        
        count = 0
        for i in range(n):
            for j in range(m):
                count += grid[i][j]

        return count
