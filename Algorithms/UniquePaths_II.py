class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid[0][0] == 1: return 0  # [1]
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        res = [[0]*n for _ in range(m)]
        res[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:  # [2]
                    if i > 0:  # [3]
                        res[i][j] += res[i - 1][j]
                    if j > 0:  # [3]
                        res[i][j] += res[i][j - 1]
        return res[-1][-1]