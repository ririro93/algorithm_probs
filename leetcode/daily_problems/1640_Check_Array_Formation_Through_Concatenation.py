class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        heads = {}
        for i, piece in enumerate(pieces):
            heads[piece[0]] = i
        print(heads)
        
        tmp = 0
        for i in range(len(arr)):
            # mid list
            print('arr[i]: ', arr[i])
            if tmp > 0: 
                print(1)
                if arr[i] == pieces[tmp_index][-tmp]:
                    tmp -= 1
                    continue
                else:
                    return False                   
            # check head of list
            elif arr[i] in heads:
                print(2)
                tmp = len(pieces[heads[arr[i]]]) - 1
                tmp_index = heads[arr[i]]
            else:
                print(3)
                return False
        return True
                
                    
            