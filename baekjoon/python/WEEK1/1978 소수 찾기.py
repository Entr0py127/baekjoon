def check_prime(a):
    if (a == 1):
        return 0;
    for i in range(2,a):
        if(not(a%i)):
            return 0
    return 1
n=input()
arr = list(map(int,input().split()))
sum=0
for i in arr:
    sum+=check_prime(i)
print(sum)

