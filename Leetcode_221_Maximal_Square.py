def solve(x: int, y: int, grid, mp):
    if y < 0 or y >= len(grid) or x >= len(grid[0]) or x < 0 or grid[y][x] == "0":
        return 0
    currentKey = str(x) + "_" + str(y)
    if currentKey in mp:
        return mp[currentKey]
    down = 1 + solve(x, y + 1, grid, mp)
    right = 1 + solve(x + 1, y, grid, mp)
    dr = 1 + solve(x + 1, y + 1, grid, mp)
    mp[currentKey] = min(down, right, dr)
    return mp[currentKey]
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = []
        mp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    area.append(solve(j, i, matrix, mp) ** 2)
        if len(area) == 0:
            return 0
        return max(area)
