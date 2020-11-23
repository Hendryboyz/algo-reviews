def find_factorial_recursive(number):
    if number == 2:
        return 2
    else:
        return number * find_factorial_recursive(number - 1)

def find_factorial_iterative(number):
    answer = number
    for i in range(2, number):
        answer *= i
    return answer

def find_fibonacci_recursive(number):
    if number == 0 or number == 1:
        return number
    else:
        return find_fibonacci_recursive(number - 1) + find_fibonacci_recursive(number - 2)

def find_fibonacci_iterative(number):
    if number == 0 or number == 1:
        return number
    prev1 = 0
    prev2 = 1
    answer = 0
    for i in range(2, number + 1):
        answer = prev1 + prev2
        prev1 = prev2
        prev2 = answer
    return answer
