#https://leetcode.com/problems/climbing-stairs/
def solve(currentStair, targetStair, dic):
    if currentStair == targetStair:
        return 1
    elif currentStair > targetStair:
        return 0
    if currentStair in dic:
        return dic[currentStair]
    oneStep = solve(currentStair + 1, targetStair, dic)
    twoSteps = solve(currentStair + 2, targetStair, dic)
    dic[currentStair] = oneStep + twoSteps
    return oneStep + twoSteps
class Solution:
    def climbStairs(self, n: int) -> int:
        return solve(0, n, dict())
