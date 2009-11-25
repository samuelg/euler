import time

then = time.time()

sum = 0

# ver 1
#for n in range(3,1000):
#	if not n % 3 or not n % 5:
#		sum += n

# ver 2
for n in range(3,1000,3):
	sum += n
for n in range(5,1000,5):
	sum += n
for n in range(15,1000,15):
	sum -= n

print 'sum = %s' % sum
print 'runtime %s' % (time.time() - then)
