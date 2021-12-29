def solve(current_index: int, prices: list, buy: bool, mp, fee):
    if current_index >= len(prices):
        return 0
    currentKey = (current_index, buy)
    if currentKey in mp:
        return mp[currentKey]
    if not buy:
        add = -prices[current_index] + solve(current_index + 1, prices, True, mp, fee)
    else:
        add = prices[current_index] + solve(current_index + 1, prices, False, mp, fee) - fee
    notadd = solve(current_index + 1, prices, buy, mp, fee)
    mp[currentKey] = max(add, notadd)
    return mp[currentKey]
class Solution:
    def maxProfit(self, prices, fee) -> int:
        return solve(0, prices, False, {}, fee)
