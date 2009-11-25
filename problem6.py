# dumb approach
import time
then = time.time()

def sum_list(nums):
    """ Sums all the numbers in a list. """
    return reduce(lambda x,y: x + y, nums)

square_sum = sum_list(range(1,101))** 2
sum_squares = sum_list([x**2 for x in range(1,101)])

print 'difference = %s' % str(square_sum - sum_squares)
print 'runtime %s' % (time.time() - then)
