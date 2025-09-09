def check_prime(p):
    for i in range(2,int(p**0.5)+1):
        if not(p%i):
            return False
    return True
def find_near_prime(num,len):
    a=0
    b=len-1
    while True :
        key=int((a+b)/2)
        if((prime[key] <= num) & (prime[key + 1] > num)):
           # print(prime[key])
            return key
        elif(prime[key] < num):
            a=key+1
        elif(prime[key + 1] > num):
            b=key-1

t=int(input())
prime=[]
for p in range(2,10001):
    if check_prime(p):
        prime.append(p)
len=len(prime)
for i in range(t):
    num=int(input())
    for r in reversed(range(find_near_prime(num/2,len)+1)):
        if num-prime[r] in prime:
            print(prime[r],num-prime[r])
            break
        r+=1
