def sum_two_smallest_numbers(numbers):
    ans = min(numbers)
    numbers.remove(min(numbers))
    return ans + min(numbers)

print(sum_two_smallest_numbers([1, 2, 3, 4, 5, 6]))