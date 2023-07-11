# 1-Countdown
def countdown(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result
print(countdown(5))  # Output: [5, 4, 3, 2, 1, 0]

# 2-Print and Return
def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
result = print_and_return([10, 20])  # Output: 10 (printed) | Result: 20 (returned)
print(result)  # Output: 20

# 3-First Plus Length
def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([2, 4, 6]))  # Output: 5 (2 + 3)

# 4-Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False

    second_value = lst[1]
    new_list = [x for x in lst if x > second_value]
    print("Number of values greater than the second value:", len(new_list))
    return new_list
result = values_greater_than_second([5, 2, 7, 9, 3, 1])
# Output: Number of values greater than the second value: 4
# Result: [5, 7, 9, 3]
print(result)

# 5-This Length, That Value
def length_and_value(size, value):
    return [value] * size
print(length_and_value(3, 7))  # Output: [7, 7, 7]
