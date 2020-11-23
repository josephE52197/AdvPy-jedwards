#!/user/bin/env python3

import sys

def answer(nums, alph):
    nums.sort()
    a = str(nums[0])
    b = str(nums[1])
    c = str(nums[2])
    if alph == "ABC": 
        return a + ' ' + b + ' ' + c
    elif alph == "ACB":
        return a + ' ' + c + ' ' + b
    elif alph == "BAC":
        return b + ' ' + a + ' ' + c
    elif alph == "BCA":
        return b + ' ' + c + ' ' + a
    elif alph == "CAB":
        return c + ' ' + a + ' ' + b
    elif alph == "CBA":
        return c + ' ' + b + ' ' + a

def solve():
    input_string = input()
    nums = input_string.split()
    nums = [int(i) for i in nums]
    alph = str(input())
    print(answer(nums,alph))

def test():
    input1 = [8,3,1]
    alph1 = "ABC"
    assert answer(input1,alph1) == "1 3 8"
    input2 = [4,2,5]
    alph2 = "BCA"
    assert answer(input2,alph2) == "4 5 2"
    input3 = [9,2,7]
    alph3 = "ACB"
    assert answer(input3,alph3) == "2 9 7"
    print("all test cases passed...")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()