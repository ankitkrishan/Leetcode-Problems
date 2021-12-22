def solve(current_index: int, coins: list, amount: int, current_amount, mp: dict):
    if current_index >= len(coins):
        return 1000000
    if current_amount == amount:
        return 0
    currentKey = str(current_index) + str(current_amount)
    if currentKey in mp:
        return mp[currentKey]
    add = 1000000
    if current_amount + coins[current_index] <= amount:
        add = 1 + solve(current_index, coins, amount, current_amount + coins[current_index], mp)
    notadd = solve(current_index + 1, coins, amount, current_amount, mp)
    mp[currentKey] = min(add, notadd)
    return mp[currentKey]
class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        ans = solve(0,  coins, amount, 0, {})
        if ans == 1000000:
            return -1
        return ans
