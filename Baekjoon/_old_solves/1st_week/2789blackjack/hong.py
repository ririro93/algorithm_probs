n, m = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

s = 0

def bruteforce(i, cur_val, num_of_cards):
    if cur_val > m:
        return 0
    if num_of_cards == 3:
        return cur_val
    r = 0
    for j in range(i+1, n):
        r = max(r, bruteforce(j, cur_val+numbers[j], num_of_cards+1))
    return r


print(bruteforce(-1, 0, 0))
