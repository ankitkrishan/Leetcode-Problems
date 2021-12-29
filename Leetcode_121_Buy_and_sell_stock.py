def solve(current_index: int, prices: list, buy: bool, transaction_count: int, mp):
    if current_index >= len(prices) or transaction_count == 1:
        return 0
    currentKey = (transaction_count, current_index, buy)
    if currentKey in mp:
        return mp[currentKey]
    if not buy:
        add = -prices[current_index] + solve(current_index + 1, prices, True, transaction_count, mp)
    else:
        add = prices[current_index] + solve(current_index + 1, prices, False, transaction_count + 1,mp)
    notadd = solve(current_index + 1, prices, buy, transaction_count, mp)
    mp[currentKey] = max(add, notadd)
    return mp[currentKey]
class Solution:
    def maxProfit(self, prices) -> int:
        return solve(0, prices, False, 0, {})
