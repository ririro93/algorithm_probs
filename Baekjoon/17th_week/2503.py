from sys import stdin, setrecursionlimit

# stdin = open('input.txt', 'r')
input = stdin.readline

# functions
def check_answer(num_list):
    global result
    for answer, strike, ball in Answers:
        strike_cnt = 0
        a, b, c = int(str(answer)[0]), int(str(answer)[1]), int(str(answer)[2])
        if a == num_list[0]:
            strike_cnt += 1
        if b == num_list[1]:
            strike_cnt += 1
        if c == num_list[2]:
            strike_cnt += 1
        ball_cnt = len(set(num_list) & set([a, b, c])) - strike_cnt

        if strike_cnt != strike:
            return
        if ball_cnt != ball:
            return
    result += 1


def backtrack(n, num_list):
    if n == 3:
        # print(num_list)
        check_answer(num_list)
        return
    for i in range(1, 10):
        if not checked[i]:
            checked[i] = True
            backtrack(n+1, num_list+[i])
            checked[i] = False

# inputs
N = int(input())
Answers = [list(map(int, input().split())) for _ in range(N)]

# init
result = 0
checked = [-1] + [0] * 9

# exec
backtrack(0, [])
print(result)


        




