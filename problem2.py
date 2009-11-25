import time

then = time.time()

def fibonacci(evens, numbers):
	number = numbers[-2] + numbers[-1]
	if number < 4000000:
		numbers.append(number)
		if not number % 2:
			evens.append(number)	
		fibonacci(evens, numbers)

evens = [2]
numbers = [1,2]

fibonacci(evens, numbers)

sum = 0
for n in evens:
	sum += n

print 'sum = %s' % sum
print 'runtime %s' % (time.time() - then)

