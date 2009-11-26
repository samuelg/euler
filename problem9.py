import time
from math import floor, sqrt
then = time.time()

def pythagorian(a, b, c):
    """ returns True if the values meet the pythagorian theorum """
    return a**2 + b**2 == c**2

def calculate(numbers):
    """ finds the values x, y, z that match x + y + z = 1000 and meet the pythagorian theorum
        z = 1000 - x - y and x < y < z
    """
    for x in numbers:
        for y in numbers:            
            if pythagorian(x, y, 1000 - x - y):
                return (x,y,1000 - x - y)

if __name__ == '__main__':
    # first triplet starts with 3
    result = calculate(range(3, 500))

    print 'result = %s, product = %s' % (result, reduce(lambda x, y: x * y, result))
    print 'runtime %s' % (time.time() - then)
