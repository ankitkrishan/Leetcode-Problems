def solve(x: int, y: int, grid, mp):
    if x == (len(grid[0]) - 1) and y == (len(grid) - 1):
        return 0
    currentKey = str(x) + "_" + str(y)
    if currentKey in mp:
        return mp[currentKey]
    right = 10000
    bottom = 10000
    if (x + 1) != len(grid[0]):
        right = grid[y][x + 1] + solve(x + 1, y, grid, mp) 
    if (y + 1) != len(grid):
        bottom = grid[y + 1][x] + solve(x, y + 1, grid, mp)
    mp[currentKey] = min(right, bottom)
    return mp[currentKey]
class Solution:
    def minPathSum(self, grid):
        return grid[0][0] + solve(0, 0, grid, {})
