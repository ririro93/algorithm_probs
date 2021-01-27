import sys
from collections import deque

# get inputs
F, S, G, U, D = map(int, input('').split(' '))

# initialization    
curr = S
checked = [False] * (F+1)
deck = deque()
deck.append(curr)
counter = 0


# # execution
# if start = goal -> finish
if G - S == 0: 
    print(0)
    sys.exit()
    
while deck:
    # print("deck: ", deck)
    # print("checked: :", checked)
    curr = deck.pop()
    counter += 1
    # print("counter1: ", counter, "\n")
    
    # if need to go up use U buton first
    if G - curr > 0:
        directions = [-D, U]
    elif G - curr < 0:
        directions = [U, -D]
    else:
        print(counter)
        sys.exit()
    
    # go up and down and add to stack
    for direction in directions:
        nex = curr + direction
        if nex == G:
            print(counter)
            sys.exit()
        elif nex >= 1 and nex <= F and not checked[nex]:
            deck.append(nex)
            checked[nex] = True
print("use the stairs")
            
        
                    

    
    
        
