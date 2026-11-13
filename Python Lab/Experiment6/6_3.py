print("Parth Dagar URN:25813561")
def filter_even_square(numbers):
    return [num**2 for num in numbers if num % 2 == 0]

nums = [1, 2, 3, 4, 5, 6]
result = filter_even_square(nums)
print(result)