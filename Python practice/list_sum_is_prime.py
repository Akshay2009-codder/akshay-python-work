# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

# Take input from user
numbers = int(input("How many numbers would you like to add : "))
num_list = []

for i in range(numbers):
    k = int(input("Enter number : "))
    num_list.append(k)

# Find all unique pairs whose sum is prime
prime_pairs = []

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        pair_sum = num_list[i] + num_list[j]
        if is_prime(pair_sum):
            prime_pairs.append((num_list[i], num_list[j]))

print("Pairs with prime sum:", prime_pairs)
