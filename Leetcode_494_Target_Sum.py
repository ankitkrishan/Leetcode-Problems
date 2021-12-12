#https://leetcode.com/problems/target-sum/
def solve(nums: list, n: int, target: int, sum: int, dic) -> int:
    if n == len(nums) - 1 and sum == target:
        return 1
    if n == len(nums) - 1 and sum != target:
        return 0
    currentKey = str(n) + "_" + str(sum)
    if currentKey in dic:
        return dic[currentKey]
    positive = solve(nums, n + 1, target, sum + nums[n + 1], dic)
    negative = solve(nums, n + 1, target, sum - nums[n + 1], dic)
    dic[currentKey] = positive + negative
    return positive + negative
class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:
        dic = {}
        ans =  solve(nums, -1, target, 0, dic)
        return ans
