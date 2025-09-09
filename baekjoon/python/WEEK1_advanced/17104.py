import sys
input = sys.stdin.readline
max_range=10**6
is_prime = [True]*(max_range+1)
prime= []
for i in range(2,max_range): #체 , T/F
    if(is_prime[i]):
        for j in range(i*i,max_range+1,i):
            is_prime[j]=False


for i in range(2,max_range+1): #소수만 모아놓은 LIST
    if(is_prime[i]):
        prime.append(i)

t=int(input())
for s in range(t):
    a=int(input())
    i=0
    cnt=0
    while prime[i]<=a/2:
        if(is_prime[a-prime[i]]):
            cnt+=1
        i+=1
    print(cnt)