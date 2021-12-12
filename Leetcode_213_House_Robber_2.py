#https://leetcode.com/problems/house-robber-ii/
def solve(current_index: int, costs: list, mp):
    currentKey = current_index
    if current_index >= len(costs):
        return 0
    if current_index in mp:
        return mp[currentKey]
    rob = costs[current_index] + solve(current_index + 2, costs, mp)
    notrob = solve(current_index + 1, costs, mp)
    mp[currentKey] = max(rob, notrob)
    return mp[currentKey]

class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2:
            return max(nums)
        mp = {}
        return max(solve(0, nums[:len(nums) -1 ], {}), solve(1, nums, {}))
