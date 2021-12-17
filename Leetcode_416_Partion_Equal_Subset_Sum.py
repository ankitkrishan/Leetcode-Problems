#https://leetcode.com/problems/partition-equal-subset-sum/
def solve(current_index: int, curr_sum, total_sum, nums: list, dict) -> bool:
    if curr_sum == total_sum / 2:
        return True
    if curr_sum!= total_sum / 2 and current_index + 1 >= len(nums):
        return False
    currentKey = curr_sum
    if currentKey in dict:
        return dict[currentKey]
    add = solve(current_index + 1, curr_sum + nums[current_index + 1], total_sum, nums, dict)
    notadd = solve(current_index + 1, curr_sum, total_sum, nums, dict)
    if add or notadd:
        dict[currentKey] = True
    else:
        dict[currentKey] = False
    return dict[currentKey]
class Solution:
    def canPartition(self, nums) -> bool:
        return solve(-1, 0, sum(nums), nums, {})
