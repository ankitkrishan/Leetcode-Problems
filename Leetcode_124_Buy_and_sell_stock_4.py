def solve(current_index: int, prices: list, buy: bool, transaction_count: int, mp, k: int):
    if current_index >= len(prices) or transaction_count == k:
        return 0
    currentKey = (transaction_count, current_index, buy)
    if currentKey in mp:
        return mp[currentKey]
    if not buy:
        add = -prices[current_index] + solve(current_index + 1, prices, True, transaction_count, mp, k)
    else:
        add = prices[current_index] + solve(current_index + 1, prices, False, transaction_count + 1,mp, k)
    notadd = solve(current_index + 1, prices, buy, transaction_count, mp, k)
    mp[currentKey] = max(add, notadd)
    return mp[currentKey]
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return solve(0, prices, False, 0, {}, k)
