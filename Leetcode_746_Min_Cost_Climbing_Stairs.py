#https://leetcode.com/problems/min-cost-climbing-stairs/
def solve(current, cost, dic):
    if current == len(cost):
        return 0
    elif current > len(cost):
        return 1000
    if current in dic:
        return dic[current]
    dic[current] = min(cost[current] + solve(current + 1, cost, dic), cost[current] + solve(current + 2, cost, dic))
    return dic[current]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        a = solve(0, cost, dic)
        b = dic[1]
        return min(a, b)
