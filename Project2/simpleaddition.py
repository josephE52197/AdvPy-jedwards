#!/usr/bin/env python3

import sys

def answer(a,b):
    return(a+b)

def test():
    assert(answer(69,420) == 489)
    assert(answer(234,1123) == 1357)
    assert(answer(5311,11111111) == 11116422)
    print("all test cases passed...")

def solve():
    a = int(input())
    b = int(input())
    print(answer(a,b))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()