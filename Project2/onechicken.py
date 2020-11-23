#!/usr/bin/env python3

import sys

def answer(n,m):
    if m-n < 0:
        if m-n == -1:
            return "Dr. Chaz needs 1 more piece of chicken!"
        else:
            return "Dr. Chaz needs " + str(-(m-n)) + " more pieces of chicken!"
    else:
        if m - n == 1:
            return "Dr. Chaz will have 1 piece of chicken left over!"
        else:
            return "Dr. Chaz will have " + str(m-n) + " pieces of chicken left over!"

def test():
    assert(answer(55,75) == "Dr. Chaz will have 20 pieces of chicken left over!")
    assert(answer(99,100) == "Dr. Chaz will have 1 piece of chicken left over!")
    assert(answer(55,54) == "Dr. Chaz needs 1 more piece of chicken!")
    print("all test cases passed...")

def solve():
    n,m = map(int, input().strip().split(" "))

    print(answer(n,m))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()