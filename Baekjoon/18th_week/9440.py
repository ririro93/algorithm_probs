from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

while True:
    # inputs
    A = list(map(int, input().split()))
    N, nums = A[0], A[1:]
    if N == 0:
        break
    
    # init
    nums.sort()
    zero_cnt = nums.count(0)
    a = b = ''
    i = 0

    # exec
    while len(a) + len(b) < N:
        if len(a) == len(b):
            if a == '':
                a += str(nums[zero_cnt])
            else:
                while i == zero_cnt or i == zero_cnt+1:
                    i += 1
                a += str(nums[i])
                i += 1
        else:
            if b == '':
                b += str(nums[zero_cnt+1])
            else:
                while i == zero_cnt or i == zero_cnt+1:
                    i += 1
                b += str(nums[i])
                i += 1
    print(int(a) + int(b))
    
