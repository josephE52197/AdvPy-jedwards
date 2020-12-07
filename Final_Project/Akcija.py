import sys

def answer(prices):
    total = 0
    temp = 0
    prices.sort(reverse=True)
    for i in range(len(prices)):
        temp += 1
        if(temp % 3 == 0):
            continue
        total += prices[i]
    return total

def test():
    input1 = [1,4,7,4,2,7]
    input2 = [6,9,4,2,0]
    input3 = [1,3,3,7,8,0,0,8,2]
    assert(answer(input1) == 20)
    assert(answer(input2) == 17)
    assert(answer(input3) == 23)
    print("all test cases passed...")

def solve():
    n = int(input())
    prices = [int(input()) for _ in range(n)]
    print(answer(prices))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()