T=int(input())
for _ in range(T):
    r,s=input().split()
    r=int(r)
    for i in range(len(s)):
        for _ in range(r):
            print(s[i],end='')
    print()
