class Solution:
    def uniquePaths(self, m, n):
        grid = [[1 for _ in range(m)] for __ in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        return grid[-1][-1]