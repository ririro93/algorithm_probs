def f(N,i):
 if N > 1:
  f(N-1,G[i][0])
  ans.append(i)
  f(N-1,G[i][1])
 else:
  ans.append(i)
 return

D = ["1 3","2 3","1 2","3 1","3 2","2 1"]
x,y,z = 0,1,2
a,b,c = 3,4,5
G={x:[z,y],y:[c,x],z:[x,b],a:[b,c],b:[a,z],c:[y,a]}

ans = []
f(int(input()),x)
print(len(ans))
for a in ans:
 print(D[a])