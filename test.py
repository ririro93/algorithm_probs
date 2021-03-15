import math

a = [0, 0]
b = [3, 6]
c = [9, 9]
def angle(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return math.degrees(math.atan2(dy, dx))

print(angle(a, b))
print(angle(b, c))
print(math.sqrt(4))