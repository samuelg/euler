import time
from math import sqrt
from math import floor

then = time.time()

def isPrime(num, primes):	
	if num not in primes:
		primes.append(num) # assume it is a prime
		for n in range(2,int(floor(sqrt(num))) + 1):
			if not num % n:
				primes.pop()
				break
	return primes

def primeFactor(num):	
	found, primes, n = False, [2,3], 2
	while found != True:
		primes = isPrime(n, primes)
		if n in primes and not num % n:
			num = int(floor(num / n))			
			primes = isPrime(num, primes)
			if num in primes:
				found = True
			else:
				n = 2
		else:
			n += 1
	return num

number = 600851475143
#number = 13195

print 'factorizing'
factor = primeFactor(number)

print 'largest prime factor for %d is %d' % (number, factor)
print time.time() - then
