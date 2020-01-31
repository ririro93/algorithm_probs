#!/usr/bin/env python
# coding: utf-8

# ## 문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# ## 입력
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

# ## 출력
# 첫째 줄에 다음 세 가지 중 하나를 출력한다.
# 
# A가 B보다 큰 경우에는 '>'를 출력한다. <br>
# A가 B보다 작은 경우에는 '<'를 출력한다. <br>
# A와 B가 같은 경우에는 '=='를 출력한다. <br>

# ## 예제입력, 예제출력
# 10 5 <br>
# \>
# <br>
# 5 5 <br>
# \=\=

# In[6]:


user_input = input()
space_index = user_input.find(" ")
A = int(user_input[:space_index])
B = int(user_input[space_index:])
if A > B:
    print(r">")
elif A == B:
    print(r"==")
else:
    print(r"<")


# In[ ]:




