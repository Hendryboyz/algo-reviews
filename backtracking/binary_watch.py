# LeetCode 401. https://leetcode.com/problems/binary-watch/

result = []
def binary_watch(n):
  watch = 0
  next(watch, 0, n)
  print([format_to_watch(time) for time in result])

def next(watch, digit, remaining):
  if digit > 9:
    return
  if remaining == 0:
    result.append(watch)
    return
  next(watch, digit + 1, remaining)
  watch += ( 1 << (9 - digit) )
  next(watch, digit + 1, remaining - 1)

def format_to_watch(time):
  watch = '{0:010b}'.format(time)
  hour = watch[0:4]
  minute = watch[4:]
  return f'{hour}:{minute}'

binary_watch(1)

  