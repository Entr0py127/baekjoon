n,r,c=map(int,input().split())
ans=0
for i in reversed(range(n)):
    p=2**i
    a=r//p
    b=c//p
    ans+=(p**2)*(a*2+b)
    r=r%(p)
    c=c%(p)
print(ans)