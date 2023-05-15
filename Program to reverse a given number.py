def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number = number // 10
    
    return reversed_num

# Example usage:
number = 12345
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
