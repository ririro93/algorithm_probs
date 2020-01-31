########## 재미로 배열로 한번 구현해보기

# get user inputs
default_str = input('')
num_steps = int(input(''))

# initiation
my_list = list(default_str)

# print(my_list)
cursor = len(my_list) - 1
inputs = [0] * num_steps
for index in range(num_steps):
    inputs[index] = input('')

# execution
for val in inputs:
    # print('former cursor: ', cursor)
    if val == 'L':
        if cursor >= 0:
            cursor -= 1
            
    if val == 'D':
        if cursor < len(my_list) - 1:
            cursor += 1
            
    if val == 'B':
        if cursor >= 0:
            my_list.pop(cursor)
            cursor -= 1
            
    if val[0] == 'P':
        _, data = val.split(' ')
        my_list.insert(cursor+1, data)
        cursor += 1
        
print(''.join(my_list))