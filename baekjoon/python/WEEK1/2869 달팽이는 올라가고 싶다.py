a,b,v=map(int,input().split())
d=(v-a)/(a-b)+1
if(d==int(d)): print(int(d))
else: print(int(d)+1)