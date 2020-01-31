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
count = 0
point = 0

# execution
for val in my_input:
    if val == '(':
        stack.append('(')
    elif val == ')':
        temp = stack.pop()
        if temp == '(':
            stack.append('*')
        else:
            while temp == '*':
                count += 1
                temp = stack.pop()
            point += count + 1

            while count > 0:
                stack.append('*')
                count -= 1
            
# print('my_input: ', my_input)
# print('stack: ', stack.data)
print(point)  

