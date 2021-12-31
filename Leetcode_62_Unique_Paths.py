def solve(x: int, y: int, m: int, n: int, mp):
    if x == (m - 1) and y == (n - 1):
        return 1
    currentKey = str(x) + "_" + str(y)
    if currentKey in mp:
        return mp[currentKey]
    right = 0
    bottom = 0
    if (x + 1) != m:
        right = solve(x + 1, y, m, n, mp) 
    if (y + 1) != n:
        bottom = solve(x, y + 1, m, n, mp)
    mp[currentKey] = right + bottom
    return mp[currentKey]
class Solution:
    def uniquePaths(self, m: int, n: int):
        return solve(0, 0, m, n, {})
