# linked list 로 첨 구현해보기
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.start_node = None
        
    def get_length(self):
        listLen = 0
        n = self.start_node
        while n is not None:
            n = n.ref
            listLen += 1
        return listLen
        
    def traverse_list(self):
        printArr = []
        n = self.start_node
        while n is not None:
            printArr.append(n.item)
            n = n.ref
        print(''.join(printArr))
        
    def insert_at_index(self, index, data):
        # 빈 리스트 
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        
        # 맨 앞에 노드 추가
        if index == 0:
            self.start_node = new_node
            new_node.ref = n
            return
            
        ## 앞에 노드 있을 때  
        for _ in range(index - 1):
            n = n.ref
        # 뒤에 노드 없어
        if n.ref is None:
            n.ref = new_node
            return
        else:
        # 뒤에 노드 있을 때
            new_node.ref = n.ref
            n.ref = new_node
        return
    
    def erase_at_index(self, index):
        n = self.start_node
        
        # 첫 노드
        if index == 0:
            self.start_node = n.ref
            return
        
        # 낀 노드
        for _ in range(index - 1):
            n = n.ref
        if n.ref.ref is None:
            n.ref = None
            return
        else:
            n.ref = n.ref.ref
            return

# get user inputs
myStr = input('')
numSteps = int(input(''))

myList = list(myStr)
myList.reverse()

# initiate
myLl = LinkedList()
for val in ''.join(myList):
    myLl.insert_at_index(0, val)

inputs = [0]*numSteps

# cursor 은 index 값 오른쪽에 있음, -1 이면 맨 왼쪽에 있음
cursor = len(myStr) - 1


# editor
for i in range(numSteps):
    inputs[i] = input('')

for myInput in inputs:
    # 왼쪽으로 이동, 맨 왼쪽이면 이동안함
    if myInput[0] == 'L':
        if cursor >= 0:
            cursor -= 1
                    
    # 오른쪽으로 이동, 리스트 끝부분이면 이동안함
    elif myInput[0] == 'D':
        if cursor < myLl.get_length() - 1:
            cursor += 1
    # 왼쪽 삭제
    elif myInput[0] =='B':
        if cursor >= 0:
            myLl.erase_at_index(cursor)
            cursor -= 1
            
    # 왼쪽에 추가
    elif myInput[0] == 'P':
        _, insertStr = myInput.split(' ')
        myLl.insert_at_index(cursor+1, insertStr)
        cursor += 1

myLl.traverse_list()









        