from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
my_input = input().split()
if len(my_input) == 2:
    H, letters = my_input
else:
    H = my_input[0]
    letters = ''
H = int(H)

# init
start = 1

# exec
for letter in letters:
    if letter == 'L':
        start = 2*start
    else:
        start = 2*start + 1

print(2**(H+1) - start)