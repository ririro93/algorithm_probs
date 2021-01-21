from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# function
def hanoi(n):
    mid = [[1, 3]]
    result = []
    if n == 1:
        return [[1, 3]]
    else:
        new_moves1 = []
        new_moves2 = []
        for i, move in enumerate(hanoi(n-1)):
            # 2는 3으로 3은 2로 바꿔주기
            new_move1 = []
            new_move2 = []
            for x in move:
                if x == 1:
                    new_move1.append(1)
                    new_move2.append(2)
                elif x == 2:
                    new_move1.append(3)
                    new_move2.append(1)
                else:
                    new_move1.append(2)
                    new_move2.append(3)
            new_moves1.append(new_move1)
            new_moves2.append(new_move2)
        result = new_moves1 + mid + new_moves2
    return result

# exe
ans = hanoi(N)
print(len(ans))
for x in ans:
    print(*x, sep=' ')