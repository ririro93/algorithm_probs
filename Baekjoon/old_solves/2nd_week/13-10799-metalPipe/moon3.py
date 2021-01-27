# initialization
my_input = input('')
new_input = my_input.replace('()', '*')

num_pipes = 0
points = 0

## execution
# '(': 파이프 1 더하기,
# '*': 점수에 파이프 개수 더하기,
# ')': 파이프 1 빼고, 점수 1 더하기

for index, val in enumerate(new_input[:-1]):
    if val == "(":
        num_pipes += 1
    elif val == "*":
        points += num_pipes
    else:
        num_pipes -= 1
        points += 1
        
# 마지막 ')' 조각 더하기
points += 1
print(points)


