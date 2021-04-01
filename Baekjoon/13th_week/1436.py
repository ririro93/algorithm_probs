from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())

# init
evil_num = 666
evil_set = {evil_num}

# exec
# abcd666 abc666d ab666cd a666bcd 666abcd 다 set에 넣기
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                evil_set |= {(a * 10**6) + (b * 10**5) + (c * 10**4) + (d * 10**3) + evil_num}
                evil_set |= {(a * 10**6) + (b * 10**5) + (c * 10**4) + (d * 10**0) + evil_num * 10}
                evil_set |= {(a * 10**6) + (b * 10**5) + (c * 10**1) + (d * 10**0) + evil_num * 10**2}
                evil_set |= {(a * 10**6) + (b * 10**2) + (c * 10**1) + (d * 10**0) + evil_num * 10**3}
                evil_set |= {(a * 10**3) + (b * 10**2) + (c * 10**1) + (d * 10**0) + evil_num * 10**4}
evil_list = list(evil_set)
evil_list.sort()
print(evil_list[N-1])