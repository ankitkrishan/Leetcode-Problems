def solve(current_index: int, prices: list, buy: bool, mp):
    if current_index >= len(prices):
        return 0
    currentKey = (current_index, buy)
    if currentKey in mp:
        return mp[currentKey]
    if not buy:
        add = -prices[current_index] + solve(current_index + 1, prices, True, mp)
    else:
        add = prices[current_index] + solve(current_index + 2, prices, False, mp)
    notadd = solve(current_index + 1, prices, buy, mp)
    mp[currentKey] = max(add, notadd)
    return mp[currentKey]
class Solution:
    def maxProfit(self, prices) -> int:
        return solve(0, prices, False, {})
