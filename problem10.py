from math import sqrt
from math import floor
import time
then = time.time()

def is_prime(num):	
    """ Determines if num is a prime.
    """
    # only test up to square root of number
    for n in range(2,int(floor(sqrt(num))) + 1):
        if not num % n:
            return False
    return True

if __name__ == '__main__':
    # start with 3 since we already know 2 is a prime.
    # only consider odd numbers, since all even numbers
    # will be divisible by 2
    primes = [2]
    primes += [x for x in range(3,2000000,2) if is_prime(x)]

    print 'result = %s' % sum(primes)
    print 'runtime %s' % (time.time() - then)
