import time
then =  time.time()

found = False
test = 20
increment = 20

numbers = []
for n in range(increment,1,-1):
	redundants = [i % n for i in numbers]
	if 0 not in redundants:
		numbers.append(n)

numbers.sort()
print numbers

while found != True:
	for n in numbers:		
		if test % (n) != 0:
			test += increment
			break
		elif n == increment:
			found = True			

print 'result = %s' % test
print 'runtime %s' % (time.time() - then)
