def solve(current_index: int, coins: list, amount: int, current_amount, mp: dict):
    if current_index >= len(coins):
        return 0
    if current_amount == amount:
        return 1
    currentKey = str(current_index) + "_" + str(current_amount)
    if currentKey in mp:
        return mp[currentKey]
    add = 0
    if current_amount + coins[current_index] <= amount:
        add = solve(current_index, coins, amount, current_amount + coins[current_index], mp)
    notadd = solve(current_index + 1, coins, amount, current_amount, mp)
    mp[currentKey] = add + notadd
    return mp[currentKey]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = solve(0,  coins, amount, 0, {})
        return ans
