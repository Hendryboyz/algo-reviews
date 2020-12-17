import collections
'''
LeetCode 198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on
the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''
def rob(nums: [int]) -> int:
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  if len(nums) == 2:
    return max(nums[0], nums[1])
  rob_max = [nums[0], max(nums[0], nums[1])] + [0] * (len(nums) - 2)
  for i in range(2, len(nums)):
    rob_max[i] = max(nums[i] + rob_max[i - 2], rob_max[i - 1])
  return rob_max[-1]
