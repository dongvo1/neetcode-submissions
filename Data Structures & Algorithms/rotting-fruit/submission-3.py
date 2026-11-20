class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def check():
            cnt = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        cnt += 1
            return cnt
        
        prev = check()
        ans = 0
        while prev:
            tmpgrid = [[grid[j][k] for k in range(len(grid[0]))] for j in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if i >= 1 and grid[i-1][j] == 1:
                            tmpgrid[i-1][j] = 2
                        if i < len(grid)-1 and grid[i+1][j] == 1:
                            tmpgrid[i+1][j] = 2
                        if j >= 1 and grid[i][j-1] == 1:
                            tmpgrid[i][j-1] = 2
                        if j < len(grid[0]) -1 and grid[i][j+1] == 1:
                            tmpgrid[i][j+1] = 2
            grid = tmpgrid
            cur = check()
            ans += 1
            if cur == 0 or cur == prev:
                break
            prev = cur
    
            
        if check():
            return -1
        return ans