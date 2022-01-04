def solve(current_number: int, n: int, k: int, target: int, sum: int, mp: dict):
    if n == 0:
        if sum == target:
            return 1
        if sum != target:
            return 0
    currentKey = (n, sum)
    if currentKey in mp:
        return mp[currentKey]
    add = 0
    ans = 0
    for i in range(1, k + 1):
        add = solve(i, n - 1, k, target, sum + i, mp)
        ans += add
    mp[currentKey] = ans
    return mp[currentKey] % (10 ** 9  + 7)
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int):
        return solve(0, n, k, target, 0, {})
