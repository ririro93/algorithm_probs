a = open('change.out', 'r')
b = open('2091_result.txt', 'r')

for i in range(1005):
    A = a.readline()
    B = b.readline()
    if A != B:
        print(i+1)
        print(A)
        print(B)
    