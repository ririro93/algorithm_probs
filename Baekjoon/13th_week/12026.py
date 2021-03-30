from sys import stdin

# stdin = open('input.txt', 'r')
input = stdin.readline

# inputs
N = int(input())
S = input().rstrip()

# init
arrB = []
arrO = []
arrJ = []
result = [0] * N
mx = 10 ** 7

# exec
for i, s in enumerate(S):
    if s == 'B':
        if i == 0:
            result[i] = 0
            arrB.append(i)
        else:
            if arrJ:
                from_J = mx
                for l in range(len(arrJ)):
                    from_J = min(from_J, result[arrJ[l]] + (i-arrJ[l]) ** 2)
                result[i] = from_J
                arrB.append(i)
            else:
                result[i] = -1

    elif s == 'O':
        from_B = mx
        for l in range(len(arrB)):
            from_B = min(from_B, result[arrB[l]] + (i-arrB[l]) ** 2) 
        result[i] = from_B
        arrO.append(i)
    else:
        if arrO:
            from_O = mx
            for l in range(len(arrO)):
                from_O = min(from_O, result[arrO[l]] + (i-arrO[l]) ** 2)
            result[i] = from_O
            arrJ.append(i)
        else:
            result[i] = -1
print(result[-1])
