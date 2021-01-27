'''
풀이1
input()은 입력의 끝에서 EOFError을 발생시킨다.


try:
    while True:
        print(sum(map(int, input().split(' '))))
except EOFError:
    pass
    
    
    
풀이2


import sys
for line in sys.stdin:
    print(sum(map(int, line.strip().split(' '))))
    
    
    
풀이3

import sys

for line in sys.stdin.readlines():
    print(sum(map(int, line.strip().split(' '))))



sys.stdin는 어떻게 interactive하게 출력??

참조
https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu
'''


import sys
for line in sys.stdin:
    print(sum(map(int, line.strip().split(' '))))
