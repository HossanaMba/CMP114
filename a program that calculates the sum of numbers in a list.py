def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    
    return total

# Example usage:
numbers = [10, 5, 7, 25, 15]
sum_of_numbers = calculate_sum(numbers)
print("The sum of numbers is:", sum_of_numbers)
