def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

primes = [num for num in range(1, 251, 2) if is_prime(num)]

# for prime in primes:
#     print(f"Prime number: {str(prime)}")

with open("prime_numbers.txt", "w") as file:
    for prime in primes:
        file.write(str(prime) + "\n")

with open("prime_numbers.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    num_words = len(words)

print(f"Number of prime numbers: {len(primes)}")
print(f"Number of words/numbers in the file: {num_words}")
