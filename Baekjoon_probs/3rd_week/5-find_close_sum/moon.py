# get inputs
n1, n2, m1, m2 = map(int, input('').split(' '))

A1 = list(map(int, input('').split(' '))).sort()
A2 = list(map(int, input('').split(' '))).sort()
B1 = list(map(int, input('').split(' '))).sort()
B2 = list(map(int, input('').split(' '))).sort()

         
# execution
s1_min = A1[0] + A2[0]
s1_max = A1[1] + A2[1]

s2_min = B1[0] + B2[0]
s2_max = B1[1] + B2[1]
