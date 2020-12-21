'''
LeetCode 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

* 1 <= nums.length <= 2 * 104
* -231 <= nums[i] <= 231 - 1
'''
def max_subarray(nums: [int]) -> int:
  subarray_sum = [0] * len(nums)
  subarray_sum[0] = nums[0]
  max_sum = nums[0]
  for i in range(1, len(nums)):
    subarray_sum[i] = max(nums[i], nums[i] + subarray_sum[i-1])
    if max_sum < subarray_sum[i]:
      max_sum = subarray_sum[i]
  return max_sum
