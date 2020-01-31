# 파이썬 내장 deque로 구현

from collections import deque

class s_deq:
    def __init__(self, num):
        self.data = deque()
        for val in range(0, num):
            self.data.append(val)
        
    def pick(self):
        return self.data.popleft()
    
    def turn_left(self):
        temp = self.data.popleft()
        self.data.append(temp)
    
    def turn_right(self):
        temp = self.data.pop()
        self.data.appendleft(temp)
        
    def print_deq(self):
        print(list(self.data))
        
# # test
# offset = 0
# deq = s_deq(5)
# deq.turn_left()
# deq.pick()
# deq.print_deq()

        
# initialization
N, M = map(int, input('').split(' '))
targets = list(map(int, input('').split(' ')))
deq = s_deq(N)
count = 0
offset = 0
# deq.print_deq()

## execution
# deque.index() time complexity: O(n) 인데 작은 상수계수래
for target in targets: #[2, 9, 5] -> new_target: [1, 8, 4] 애초에 덱 값도 0에서 시작함
    new_target = target - 1
    index = list(deq.data).index(new_target)
    if index <= N - index:
        while deq.data[0] != new_target:
            deq.turn_left()
            count += 1
        deq.pick()
        N -= 1
    else:
        while deq.data[0] != new_target:
            deq.turn_right()
            count += 1
        deq.pick()
        N -= 1
print(count)