a = int(input())
b = int(input())
_b = b
while b > 0:
    c = b % 10
    print(a*c)
    b //= 10
print(a*_b)