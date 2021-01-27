from sys import stdin

class stack:
    def __init__(self):
        self.data = []
    
    def append(self, new_data):
        self.data.append(new_data)
    
    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return -1

# initialize
my_num = int(input(''))

for _ in range(my_num):
    my_input = stdin.readline()
    my_stack = stack()
    end = False
    for val in my_input[:-1]:
        if not end:
            if val == '(':
                my_stack.append(val)
            elif val == ')':
                temp = my_stack.pop()
                if temp != '(':
                    print('NO')
                    end = True
    if (my_stack.data and not end):
        print('NO')
    elif not end:
        print('YES')
    
