from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline 

# inputs
my_string = input().strip()

# function 
def solve(my_string):
    # init
    b = ['(', ')', '[', ']'] # 괄호 종류, '(' 이런거 계속 쓰기 싫어서
    cnt1 = 0 # cnt1은 열려있는 () 수
    cnt2 = 0
    d1 = True # 괄호가 열리고 있으면 True, 닫히고 있으면 False
    d2 = False
    result = 0
    stack = [] # ( 이면 1 넣고, [ 이면 2 넣고 괄호가 맞는지 체크
    for c in my_string:
        if c == b[0]:
            stack.append(1)
            cnt1 += 1
            d1 = True
        elif c == b[1]:
            if not stack or stack[-1] != 1:
                return 0
            stack.pop()
            if d1:
                result += 2**cnt1 * 3**cnt2
                # 열려있는 []에 대해 계산을 이미 하면 계산 중복 안되게 해야됨
                if cnt2 > 0:
                    d2 = False
            cnt1 -= 1
            d1 = False
        elif c == b[2]:
            stack.append(2)
            cnt2 += 1
            d2 = True
        else:
            if not stack or stack[-1] != 2:
                return 0
            stack.pop()
            if d2:
                result += 2**cnt1 * 3**cnt2
                if cnt1 > 0:
                    d1 = False
            cnt2 -= 1
            d2 = False

    # 루프 끝나고 나머지가 없어야 안 틀린 괄호열
    if cnt1 == cnt2 == 0:
        return result
    else:
        return 0
            
# exe
print(solve(my_string))  