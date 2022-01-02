def solve(x: int, y: int, grid, mp: dict):
    if y == (len(grid) - 1):
        return grid[y][x]
    currentKey = str(x) + "_" + str(y)
    if currentKey in mp:
        return mp[currentKey]
    down = grid[y][x] + solve(x, y + 1, grid, mp)
    dr = 10000
    dl = 10000
    if (x + 1) < len(grid[0]):
        dr = grid[y][x] + solve(x + 1, y + 1, grid, mp)
    if (x - 1) >= 0: 
        dl = grid[y][x] + solve(x - 1, y + 1, grid, mp)
    mp[currentKey] = min(down, dr, dl)
    return mp[currentKey]
class Solution:
    def minFallingPathSum(self, matrix):
        ans = []
        mp = {}
        for i in range(len(matrix[0])):
            ans.append(solve(i, 0, matrix, mp))
        return min(ans)
