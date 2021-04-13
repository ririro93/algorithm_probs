from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

## 1541. 잃어버린 괄호
"""
마이너스 기호가 한번이라도 나오면 그 다음에 나오는 숫자들은 다 빼줄 수 있다
-> 처음으로 - 나오기 전까지 숫자는 다 더하고 그 후론 다 빼주면 답
"""
# inputs
S = input().rstrip()

# init
minus = False
result = 0
num = ''

# exec
for s in S:
    if s.isdigit():
        num += s
    else:
        if minus:
            if num:
                result -= int(num)
        else:
            if num:
                result += int(num)
        num = ''
    if s == '-':
        minus = True
if minus:
    result -= int(num)
else:
    result += int(num)
print(result)