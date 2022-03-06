# Write a  list  comprehension  that  generates all non-primes between 2 and 100.

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

all_primes_between_2_and_100 = [x for x in range(2, 100) if is_prime(x)]
print(all_primes_between_2_and_100)