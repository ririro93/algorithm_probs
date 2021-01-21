from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
day, night, H = map(int, input().split())

# function
def climb(day, night, H):
    speed = day - night
    goal = H - day
    q, r = divmod(goal, speed)
    if r:
        return q + 2
    else:
        return q + 1
    
# exe
print(climb(day, night, H))