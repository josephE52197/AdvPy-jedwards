import sys

def answer(n,m,nums):
    ans = ""
    for i in range(n):
        if i not in nums:
            ans += (str(i) +"\n")
    return (ans +"Mario got {} of the dangerous obstacles.".format(len(nums)))

def test():
    assert(answer(15,5,[4,9,2]) == "0\n1\n3\n5\n6\n7\n8\n10\n11\n12\n13\n14\nMario got 3 of the dangerous obstacles.")
    assert(answer(10,4,[1,2,3]) == "0\n4\n5\n6\n7\n8\n9\nMario got 3 of the dangerous obstacles.")
    assert(answer(9,6,[4,2,0,6]) == "1\n3\n5\n7\n8\nMario got 4 of the dangerous obstacles.")
    print("all test cases passed...")

def solve():
    n,m = map(int, input().strip().split(" "))
    nums = []
    for i in range(m):
        obst = int(input())
        if obst not in nums and obst in list(range(n)):
            nums.append(obst)
    print(nums)
    print(answer(n,m,nums)) 

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()