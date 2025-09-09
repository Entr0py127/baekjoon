t=int(input())
results=[]
for i in range(t):
    a=tuple(map(int,input().split()))
    results.append(a)
for i in range(t):
    print("%d" %(results[i][0]+results[i][1]))
