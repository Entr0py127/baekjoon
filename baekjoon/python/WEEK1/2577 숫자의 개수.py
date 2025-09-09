a,b,c=(int(input()) for _ in range(3))
arr=[0]*10
num=a*b*c
while num:
    i=num%10
    arr[i]+=1
    num=int(num/10)
for i in range(10):
    print(arr[i])
