#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

s = list(map(lambda x: ord(x) - 96, list(input(''))))
listS = [0] * 26
for ord_alpha in s:
    listS[ord_alpha - 1] += 1
print(*listS)
    