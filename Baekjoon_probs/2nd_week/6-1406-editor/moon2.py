class Node:
    def __init__(self, data):
        self.item = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    # 첨에 받는 명령 수로 cursor 값 정해버리기
    def __init__(self, length):
        self.start_node = None
        self.last_node = None
        self.temp_node = None

        self.cursor = length - 1

    def initialize(self, data_str):
        for index, value in enumerate(list(data_str)):
            n = Node(value)
            if index == 0:
                self.start_node = n
                temp_node = n
            else:
                temp_node.next = n
                n.prev = temp_node
                temp_node = n
        self.last_node = n
        self.temp_node = n
        
    # 'L' 기본적으로 커서는 임시 노드 오르쪽임; 임시 노드가 첫 노드인 경우 제외
    def cursorLeft(self): 
        if self.cursor == -1:
            return
        else:
            self.cursor -= 1
            if self.temp_node.prev is not None:
                self.temp_node = self.temp_node.prev
        
    # 'D' 
    def cursorRight(self): 
        if self.cursor == -1:
            self.cursor += 1
        elif self.temp_node.prev is None and self.temp_node.next is None:
            return
        elif self.temp_node.prev is None and self.temp_node.next is not None:
            self.temp_node = self.temp_node.next
            self.cursor += 1
        elif self.temp_node.prev is not None and self.temp_node.next is None:
            return
        else:
            self.temp_node = self.temp_node.next
            self.cursor += 1
            
        
    # 'B'    
    def erase(self):
        if not self.cursor == -1:
            if self.temp_node == self.start_node:
                if self.start_node.next is not None:
                    self.start_node = self.start_node.next
                    self.temp_node = self.start_node
                    self.temp_node.prev = None
                else:
                    self.start_node = None
            elif self.temp_node == self.last_node:
                self.last_node = self.last_node.prev
                self.temp_node = self.last_node
                self.temp_node.next = None
            else:
                # n 은 임시로 저장한 노드
                n = self.temp_node.next
                self.temp_node = self.temp_node.prev
                self.temp_node.next = n
                n.prev = self.temp_node
            self.cursor -= 1
    
    # 'P;
    def add(self, data):
        n = Node(data)
        if self.cursor == -1:
            n.next = self.start_node
            self.start_node = n
            if self.start_node.next is not None:
                self.start_node.next = self.temp_node
            else: 
                self.start_node = n
        elif self.temp_node.next is not None:
            n.prev = self.temp_node
            n.next = self.temp_node.next
            self.temp_node.next.prev = n
            self.temp_node.next = n
        else:
            self.temp_node.next = n
            self.last_node = n
            n.prev = self.temp_node
        self.temp_node = n
        self.cursor += 1
        
        
    def printList(self):
        n = self.start_node
        print_list = []
        while n is not None:
            print_list.append(n.item)
            n = n.next
        print(''.join(print_list))

# user input
user_input = input('')
user_num = int(input(''))
user_orders = [0] * user_num
for i in range(user_num):
    user_orders[i] = input('')
    
# initialize
myDll = DoubleLinkedList(len(list(user_input)))
myDll.initialize(user_input)

# execute
for order in user_orders:
    if order == "L":
        myDll.cursorLeft()
    elif order == "D":
        myDll.cursorRight()
    elif order == "B":
        myDll.erase()
    elif order[0] == "P":
        _, data = order.split(' ')
        myDll.add(data)
    # print(order)
    # myDll.printList()
    # print('cursor: ', myDll.cursor)
    # print('start: ', myDll.start_node.item)
    # print('last: ', myDll.last_node.item)
    # print('temp: ', myDll.temp_node.item, '\n')

myDll.printList()
    

            

                
                
            