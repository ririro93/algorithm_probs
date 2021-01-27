# 일단 () 붙어있는 애들을 * 이런걸로 치환해보자
# 말고 걍 비슷하게 () 붙어있으면 *이랑 같은 처리하게
class stack:
    def __init__(self):
        self.data = []
        
    def append(self, new_data):
        self.data.append(new_data)
    
    def pop(self):
        return self.data.pop()
            
#initialization
my_input = input('')
# new_input = my_input.replace('()', '*')
stack = stack()
counter_star = 0
point = 0

# change stack from ((()())()) to ((**)*)
for val in my_input:
    if val =='(':
        stack.append('(')
    elif val == ')':
        popped = stack.pop()
        if popped == '(':
            stack.append('*')
        elif popped == '*':
            stack.append('*')
            stack.append(')')
        else:
            stack.append(')')
            stack.append(')')
new_stack = ''.join(stack.data)
# print(new_stack)
# execution
for val in new_stack:
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
# print('new_stack: ', new_stack)
# print('stack: ', stack.data)
print(point)