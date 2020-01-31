n = int(input())

generator = 0
for i in range(1, n):
    _i = i
    generated_num = i
    while i > 0:
        generated_num += i % 10
        i //= 10
    if generated_num == n:
        generator = _i
        break
        
print(generator)
        