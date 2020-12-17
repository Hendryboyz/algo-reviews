'''
LeetCode 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
'''
def climbStairs(n: int) -> int:
  if n == 1 or n == 2:
    return n
  pre_previous = 1
  previous = 2
  possibility = 2
  for i in range(3, n + 1):
    possibility = previous + pre_previous
    pre_previous = previous
    previous = possibility
  return possibility
