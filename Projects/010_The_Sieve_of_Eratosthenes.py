# Generate prime numbers using the sieve of Erathosthenes algorithm
# Inspired by Computerphile: https://www.youtube.com/watch?v=bnRNiE_OVWA and https://www.youtube.com/watch?v=5jwV3zxXc8E

# Infite list of all natural numbers except 1
def nats_generator(n):
    yield n
    yield from nats_generator(n + 1)


# Stores the infinite list of all natural numbers, starting at 2
nats = nats_generator(2)


# Sieves the infinite list for primes
def sieve(numbers=nats):
    n = next(numbers)   # Select the first number from the list, it is a prime
    yield n             # Yields the prime
    yield from sieve(num for num in numbers if num % n != 0)    # Sieves all multiples of the prime from the list


# Note to self: To 'yield from' recursively, either pass the state through a parameter, like in this case OR
# modify some global variable accessible to all the generators that are recursively called by 'yield from'

primes = sieve()

print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
