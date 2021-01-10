## encoded XOR
from sys import stdin
input = stdin.readline

# function 
def sol(my_list, first):
    num = 0
    ans = [first]
    for ele in my_list:
        num = ele ^ ans[-1]
        ans.append(num)
    return ans

# inputs
l = list(map(int, input()[1:-2].split(",")))
first = int(input())

# exe
print(sol(l, first))