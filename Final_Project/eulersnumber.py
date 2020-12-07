import sys
import math

def answer(n):
    e = 0
    if n > 20: n = 20
    for i in range(0,n+1):
        e += (1 / math.factorial(i))
    return e

def test():
    assert(answer(2) == 2.5)
    assert(answer(5) == 2.7166666666666663)
    assert(answer(300) == 2.7182818284590455)
    print("all test cases passed...")

def solve():
    n = int(input())
    print(answer(n))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()