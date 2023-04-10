import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

random_number = random.randint(1, 200)
print("Random number:", random_number)

if is_prime(random_number):
    print(random_number, "is a prime number.")
else:
    print(random_number, "is not a prime number.") 