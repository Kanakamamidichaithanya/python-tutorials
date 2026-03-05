# n = int(input("enter the the number"))
# if n>2 and n<=500:
#     sum  = (n*(n+1))//2
#     print(sum)
# else:
#     print("error")

n = int(input("Enter a number: "))  # Input the range
prime_sum = 0  # Variable to store the sum

for num in range(2, n + 1):  # Iterate from 2 to n
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check if num is prime
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num  # Add prime to sum

print("Sum of prime numbers up to", n, "is:", prime_sum)
