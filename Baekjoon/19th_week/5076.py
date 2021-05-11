from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

while True:
    # inputs
    S = input().rstrip()
    if S == '#':
        break
    
    # init
    stack = []
    tmp = ''
    flag = False

    # exec
    for s in S:
        if s == '<':
            flag = True
        elif s == '>':
            if tmp[-1] != '/':
                stack.append(tmp.split(' ')[0])
            flag = False
            tmp = ''
        elif flag:
            tmp += s
        # print(stack)

        # / 가 앞에 붙은게 stack에 추가되면 stack 전꺼 보고 삭제
        if stack and stack[-1][0] == '/':
            # stack 그 전에 꺼가 없으면  illegal
            if len(stack) == 1:
                print('illegal')
                break
            # 전에 꺼를 닫는 tag 이면 둘다 stack에서 제외하고 계속
            if stack[-1][1:] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                print('illegal')
                break
    else:
        if not stack:
            print('legal')
        else:
            print('illegal')
