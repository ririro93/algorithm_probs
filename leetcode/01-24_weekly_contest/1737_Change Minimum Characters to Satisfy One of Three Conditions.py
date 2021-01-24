"""
:type a: str
:type b: str
:rtype: int
"""
def changetointlist(my_str):
    result = []
    for c in my_str:
        tmp = ord(c) - 97
        result.append(ord(c)-97)
    return result

class Solution(object):
    def minCharacters(self, a, b):
        ans = 200000
        la, lb = changetointlist(a), changetointlist(b)
        print(sorted(la))
        print(sorted(lb))
        for std in range(0, 26):
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0
            for elea in la:
                if elea != std:
                    cnt1 += 1
                if std != 0:
                    if elea >= std:
                        cnt2 += 1
                    if elea < std:
                        cnt3 += 1
                else:
                    cnt2 = cnt3 = 200000
            for eleb in lb:
                if eleb != std:
                    cnt1 += 1
                if std != 0:
                    if eleb < std:
                        cnt2 += 1
                    if eleb >= std:
                        cnt3 += 1
                else:
                    cn2 = cnt3 = 200000
            ans = min(ans, cnt1, cnt2, cnt3)
            if ans == 20:
                print(std, cnt1, cnt2, cnt3)
        return(ans)
                    
            
        
        