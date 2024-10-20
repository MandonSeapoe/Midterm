def sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_sum += num
    return even_sum

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)
