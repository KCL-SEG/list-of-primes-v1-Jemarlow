"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    list = []

    for n in range(2, 2 + number_of_primes):
        for i in range(2, n):

            isPrime = n%i != 0

            if isPrime is False:
                break

        if isPrime:
            list.append(n)

    return list