class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += 1
                    self.DFS(grid, visited, i, j)
        return res
    
    def DFS(self, grid, visited, i, j):
        if (0<=i<len(grid)) and (0<=j<len(grid[0])) and not visited[i][j] and grid[i][j] == '1':
            visited[i][j] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.DFS(grid, visited, i+dr, j+dc)