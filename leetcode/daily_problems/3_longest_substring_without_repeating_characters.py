class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. s 루프 돌면서 longest라는 리스트에 없으면 longest에 추가 -> O(n**2)
        # 2. s 루프 돌면서 각 chr를 딕셔너리에 저장하고 없으면 반환값에 추가 -> 어디까지 지워야되는지 모름
        # 3. s 루프 돌면서 각 chr를 key로 하고 인덱스값을 val로 갖는 딕셔너리 만들기
        # 4. 반복되는 애 나올 때마다 포인터를 걔 뒤에 위치에 두기
        dic = {}
        result = 0
        point = 0
        for i, c in enumerate(s):
            
            # 처음 보는 수 -> 인덱스 저장
            if c not in dic:
                dic[c] = i
                result = max(result, i - point + 1)
                
            # 본 적 있는 수
            else:
                # 포인터보다 앞에 있으면 그냥 첨 본 취급
                if dic[c] < point:
                    dic[c] = i
                    result = max(result, i - point + 1)
                    
                # 포인터보다 뒤에 있으면 
                else:
                    result = max(result, i - point)
                    point = dic[c] + 1
                    dic[c] = i
            # print(dic)
            # print('result', result)
        return result
                
    
