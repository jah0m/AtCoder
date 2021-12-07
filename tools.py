import math
from functools import reduce
#最大公约数
def gcd(*numbers):
    return reduce(math.gcd, numbers)