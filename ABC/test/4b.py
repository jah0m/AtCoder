import sys
from itertools import combinations
import math
def main(lines):
    l, r = map(int, lines[0].split())
    m = int(lines[1])
    nm = [int(x) for x in lines[2].split()]
    #最小公倍数
    def my_lcm_base(x, y):
        return (x * y) // math.gcd(x, y)

    ans = r - l + 1
    for n in nm:
        cnt = r // n - (l-1) // n
        ans -= cnt

    for a, b in combinations(nm, 2):
        c = my_lcm_base(a,b)
        cnt = r // c - (l-1) // c
        ans += cnt

    print(ans)
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
