import sys
input = sys.stdin.readline
max_range=10**6
is_prime = [True]*(max_range+1)
prime= []
for i in range(2,max_range): #체 , T/F
    if(is_prime[i]):
        for j in range(i*i,max_range+1,i):
            is_prime[j]=False


for i in range(2,max_range): #소수만 모아놓은 LIST
    if(is_prime[i]):
        prime.append(i)

t=input()
while True:
    a=int(input())
    if(a==0):
        break
    i=1
    while prime[i]<=a/2:
        if(is_prime[a-prime[i]]):
            print(a,"=",prime[i],"+",a-prime[i])
            break
        i+=1
