# 리스트로 구현 -> 예제는 다 맞음
import numpy as np

class spinning_deque:
    def __init__(self, N):
        self.data = list(np.arange(1, N+1))
    
    def pick(self):
        self.data.pop(0)
    
    def turn_left(self):
        temp = self.data.pop(0)
        self.data.append(temp)
        
    def turn_right(self):
        temp = self.data.pop()
        self.data.insert(0, temp)
        
    def print_deque(self):
        print(self.data)
    
    

# initialize
N, M = map(int, input('').split(' '))
targets = list(map(int, input('').split(' ')))
s_deq = spinning_deque(N)
count = 0

# execution
for target in targets:
    # deque에서 target을 찾아서 index 저장
    index = s_deq.data.index(target)
    
    if index <= 0.5 * len(s_deq.data):
        while s_deq.data[0] != target:
            s_deq.turn_left()
            count += 1
        s_deq.pick()
    else:
        while s_deq.data[0] != target:
            s_deq.turn_right()
            count += 1
        s_deq.pick()
print(count)
    
    
