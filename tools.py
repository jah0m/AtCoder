import math
from functools import reduce
#最大公约数
def gcd(*numbers):
    return reduce(math.gcd, numbers)
#最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
#多个数的最小公倍数
def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

#根据列表元素的第二个值进行排序
def takeSecond(elem):
    return elem[1]
#用二分法查找x在已排列的list中排第几位
import bisect
index = bisect.bisect_left(sorted_arr, x)
