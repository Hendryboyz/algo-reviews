import math
import copy

def radix_sort(array, base = 10):
    max_num = max(array)
    highest_digit = int(math.floor(math.log(max_num, base)) + 1)
    
    output = copy.copy(array)
    for i in range(highest_digit):
        output = counting_sort_digit_base(output, i, base)
    
    return output

def counting_sort_digit_base(array, digit, base):
    counting = [0] * base
    result = [0] * len(array)
    
    for i in range(len(array)):
        current_digit = (array[i] / (base**digit)) % base
        counting[current_digit] = counting[current_digit] + 1
    
    for i in range(1, len(counting)):
        counting[i] = counting[i] + counting[i - 1]
    
    for i in range(len(array) - 1, -1, -1):
        current_digit = (array[i] / (base**digit)) % base
        result_idx = counting[current_digit] - 1
        counting[current_digit] = counting[current_digit] - 1
        result[result_idx] = array[i]
    return result
