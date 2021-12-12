#https://leetcode.com/problems/house-robber/
def solve(current_index: int, costs: list, mp):
    if current_index >= len(costs):
        return 0
    if current_index in mp:
        return mp[current_index]
    rob = costs[current_index] + solve(current_index + 2, costs, mp)
    notrob = solve(current_index + 1, costs, mp)
    mp[current_index] = max(rob, notrob)
    return mp[current_index]

class Solution:
    def rob(self, nums) -> int:
        mp = {}
        return solve(0, nums, mp)
