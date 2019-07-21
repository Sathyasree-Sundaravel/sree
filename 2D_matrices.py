#2D matrix of integers
m,n=map(int,input().split())
k=[]
for i in range(0,m):
    l=[int(v) for v in input().split()]
    k.append(sorted(l))
for i in range(0,len(k[0])):
  for j in range(0,len(k)-1):
    if k[j][i]>k[j+1][i]:
      k[j][i],k[j+1][i]=k[j+1][i],k[j][i]
for i in k:
  print(*i)
