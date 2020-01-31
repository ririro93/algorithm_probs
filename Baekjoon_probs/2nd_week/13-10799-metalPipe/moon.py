# 일단 () 붙어있는 애들을 * 이런걸로 치환해보자
class stack:
    def __init__(self):
        self.data = []
        
    def append(self, new_data):
        self.data.append(new_data)
    
    def pop(self):
        return self.data.pop()
            
#initialization
my_input = input('')
new_input = my_input.replace('()', '*')
stack = stack()
counter_star = 0
point = 0

#execution
for index, val in enumerate(new_input):
    if val == '(':
        stack.append('0')
    elif val == '*':
        stack.append('*')
    elif val == ')':
        popped = stack.pop()
        while popped == '*':
            counter_star += 1
            popped = stack.pop()
        point += counter_star + 1
        
        while counter_star > 0:
            stack.append('*')
            counter_star -= 1
        

# print('my_input: ', my_input)
# print('new_input: ', new_input)
# print('stack: ', stack.data)
print(point)