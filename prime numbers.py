def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def print_prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")

# Example usage:
n = 20
print("Prime numbers up to", n)
print_prime_numbers(n)
