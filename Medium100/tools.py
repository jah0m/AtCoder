import math
from functools import reduce
#最大公约数
def gcd(*numbers):
    return reduce(math.gcd, numbers)
#根据列表元素的第二个值进行排序
def takeSecond(elem):
    return elem[1]
l.sort(key=takeSecond)