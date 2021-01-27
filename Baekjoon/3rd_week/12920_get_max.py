'''
# 주어진 리스트에서 자기랑 K번째 전 index까지 중에서 최대값 구하기
k = 3

#    답 : [5, 6, 6, 7, 7, 7, 4, 3]
my_list = [5, 6, 3, 7, 3, 4, 2, 1]
print(my_list)

my_max = [5] 

# point1 이 나이, point2가 어린 최대값 가리키는애
point1 = point2 = 0

# 현재 가능 최대값
tmp = my_list[0]

for i, ele in enumerate(my_list[1:], start=1):
    # 어린 최대값 갱신되면 포인터2 옮기기
    if ele > my_list[i-1]:
        point2 = i
    # 너무 늙으면 포인터 한칸 옮기기
    if i - point1 > k:
        point1 += 1
    # 너무 늙은 최대값은 
    if  point2 < point1:
        point2 = point1
    print(point1, point2)
    my_max.append(max(my_list[point1], my_list[point2]))
print(my_max)
'''
from collections import deque

k = 4

my_list = [10, 7, 8, 5, 6, 6, 5, 4, 3, 2, 1]
print(my_list)

tmp = -1
max_list = [my_list[0]]
deq = deque()
deq.append(my_list[0])

for i in range(1, len(my_list)):
    # 만약 맨 앞에 있는 애보다 크면 아예 초기화 해버리기
    if my_list[i] >= deq[0]:
        deq = deque()
        deq.append(my_list[i])
        tmp = -1
    else:
        if my_list[i] >= deq[-1]:
            tmp = my_list[i]
        deq.append(my_list[i])
        # 가장 중요한 기준은 덱 길이 -> 늙으면 가차없이 짜름
        if len(deq) > k:
            if tmp == deq.popleft():
                tmp = deq[0]
        # 살아남은 애중에 젤 큰애는 살아남음 왜냐면 tmp=6 
        while tmp > deq[0]:
            deq.popleft()
    max_list.append(deq[0])
    print(deq, tmp)
print(max_list)
    

        
            
    