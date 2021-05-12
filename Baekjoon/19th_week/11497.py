from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def get_ans(result):
    global N, ans

    for i in range(N-1):
        diff = abs(result[i] - result[i+1])
        ans = max(ans, diff)

##################################################
# T
T = int(input())

# Test Cases
for _ in range(T):
    # inputs
    N = int(input())
    Nums = list(map(int, input().split()))

    # init
    Nums.sort()
    front = []
    back = []
    result = []
    ans = 0

    ## exec
    for i in range(N-1):
        if i % 2 == 0:
            front.append(Nums[i])
        else:
            back.append(Nums[i])
    result = front + [Nums[-1]] + back[::-1]
    get_ans(result)
    print(ans)