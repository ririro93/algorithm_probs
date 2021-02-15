from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline


# inits
result = ''
max_len = 0
S = []

for _ in range(5):
    s = input().strip()
    max_len = max(max_len, len(s))
    S.append(s)
    
# exe
for j in range(max_len):
    for i in range(5):
        if j < len(S[i]):
            result += S[i][j]
print(result)