# 어떻게든 해볼라 했는데 이렇게 조건 하나하나 주다간 끝이 없을듯
# use as manay coins as possible 

from sys import stdin

stdin = open('input.txt')
input = stdin.readline

# inputs
P, C1, C2, C3, C4 = map(int, input().split())
C = [C1, C2, C3, C4] # [5, 3, 1, 2]
temp = C[:]

# init
coins = [1, 5, 10, 25]
result = [0] * 4

# function
def sol(P):
    cnt = 0
    pointer = 0
    up = True
    
    while C[0]>0 or C[1]>0 or C[2]>0 or C[3]>0:
        print("C: ", C, "pointer: ", pointer, "cnt: ", cnt)
        if up:
            C[pointer] -= 1
            cnt += coins[pointer]
            if cnt == P:
                return [x-y for x, y in zip(temp, C)]
            elif cnt < P:
                if C[pointer] == 0:
                    pointer += 1
            else:
                pointer -= 1
                up = False
        else:
            C[pointer] += 1
            cnt -= coins[pointer]
            if cnt == P:
                return C
            elif cnt < P:
                if C[pointer] == 0:
                    pointer += 1
                else:
                    pointer -= 1
                    up = True
            else:
                if C[pointer] == temp[pointer]:
                    pointer -= 1
                continue
    print("no")    
    return [x-y for x, y in zip(temp, C)]

# exe
print(sol(P))

        

    
    
    

