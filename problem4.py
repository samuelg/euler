import time

then = time.time()

candidates = []

for n in range(900,1000):
	for m in range(900,1000):
		if str(n * m) == str(n * m)[::-1]:
			candidates.append(n * m)

candidates.sort()
print 'palindromes %s' % str(candidates)
print 'largest palindrom is %d' % (candidates[-1])
print 'runtime %s' % (time.time() - then)
