from math import sqrt
from math import floor
import time
then = time.time()

# dumb approach, with previous values cached
# runtime 9.22 seconds on my machine
def process_prime(num, primes_cache):	
    """ Determines if num is a prime. If it was not in the cache, adds it to the cache.
        primes_cache should be initialized to [2] before first calling this function.
    """
    if num not in primes_cache:
        primes_cache.append(num) # assume it is a prime
        # only test up to square root of number
        for n in range(2,int(floor(sqrt(num))) + 1):
            if not num % n:
                primes_cache.pop()
                break
    return primes_cache

if __name__ == '__main__':
    primes_cache = [2]
    result = 0

    # start with 3 since we already know 2 is a prime.
    # only consider odd numbers, since all even numbers
    # will be divisible by 2
    for x in range(3,1000000,2):
        if len(primes_cache) == 10001:
            result = primes_cache[10000]
            break
        else:
            primes_cache = process_prime(x, primes_cache)
    
    print 'result = %s' % result
    print 'runtime %s' % (time.time() - then)
