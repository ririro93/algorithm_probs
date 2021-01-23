def move(N, start, to):
    print(N, start, to)
    
def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

hanoi(3, 'A', 'C', 'B')