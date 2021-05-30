## 짝지어 제거하기
def solution(s):
    stack = [s[0]]
    for c in s[1:]:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        answer = 0
    else: 
        answer = 1

    return answer