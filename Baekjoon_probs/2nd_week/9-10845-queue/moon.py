# # 배열 써서 큐 만들기 -> 런타임 에러
# from sys import stdin

# class MyQueue:
#     def __init__(self):
#         self.queue = []
    
#     # def initialize(se
#     #     for val in data:
#     #         self.queue.append(val)
    
#     def push(self, data):
#         self.queue.append(data)
    
#     def pop(self):
#         if len(self.queue) == 0:
#             return -1
#         else:
#             return self.queue.pop(0)
    
#     def size(self):
#         return len(self.queue)
    
#     def empty(self):
#         if self.queue == []:
#             return 1
            
#         else:
#             return 0
    
#     def front(self):
#         if self.queue:
#             return self.queue[0]
#         else:
#             return -1
    
#     def back(self):
#         if self.queue:
#             return self.queue[len(self.queue)-1]
#         else:
#             return -1
        
#     def show_queue(self):
#         print(''.join(self.queue))
    
# # execution
# my_queue = MyQueue()
# # N = int(input(''))
# # orders = []
# # for _ in range(N):
# #     orders.append(input(''))
# # print(orders)

# for _ in range(int(stdin.readline())):
#     order = stdin.readline().split()
#     if order[0] == 'push':
#         my_queue.push(order[1])
#     elif order[0] == 'pop':
#         print(my_queue.pop())
#     elif order[0] == 'size':
#         print(my_queue.size())
#     elif order[0] == 'empty':
#         print(my_queue.empty())
#     elif order[0] == 'front':
#         print(my_queue.front())
#     elif order[0] == 'back':
#         print(my_queue.back())
#     else:
#         print('wrong input')

# # my_queue.show_queue()
    

    
a = []
print(a[0] is not None)
    
    
    
    


    
    
    
    
    
    
    
    
    
    
        