# 124 나라의 숫자 

def solution(n):
    ## functions
    def get_ternary(num):
        result = ''
        q, r = divmod(num, 3)
        while q >= 1:
            q, r = divmod(num, 3)
            result = str(r) + result
            num = q
        return result or str(r)
    
    ## init
    cnt = 3
    i = 1
    while True:
        if cnt >= n:
            cnt -= 3 ** i
            break
        i += 1
        cnt += 3 ** i

    ## exec
    num = n - cnt - 1
    num_ter = get_ternary(num)

    ans = '1' * (i-len(num_ter))
    for c in num_ter:
        if c == '0':
            ans += '1'
        elif c == '1':
            ans += '2'
        else:
            ans += '4'
    return ans

# init
input =  open('input.txt', 'r').readline

# inputs
inputs = [int(input()) for _ in range(10)]

# exec
for i in range(0, len(inputs)):
    print(f'#{i+1}')
    print(solution(inputs[i]))