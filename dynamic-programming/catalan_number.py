# https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
# LeetCode 96. Unique Binary Search Trees

def n_th_catalan_number(n):
  catalan_memo = [0] * (n + 1)
  catalan_memo[0] = catalan_memo[1] = 1

  for current_n in range(2, n + 1):
    for r in range(current_n + 1):
      catalan_memo[current_n] += (catalan_memo[r - 1] * catalan_memo[current_n - r])

  return catalan_memo[n]

print(n_th_catalan_number(10))