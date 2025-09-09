n=int(input())
max=-100
sum=0
arr=list(map(int,input().split()))
used=[False]*n
def put(num,address):
    global sum,max
    if num==n:
        if sum>max:
            max=sum
    elif num==0:
        for i in range(n):
            used[i]=True
            put(num+1,i)
            used[i]=False
    else:
        for i in range(n):
            if(not used[i]):
                used[i]=True
                sum+=abs(arr[address]-arr[i])
                put(num+1,i)
                sum -= abs(arr[address] - arr[i])
                used[i]=False
put(0,-1) #사용개수 / 전에는 뭘 썼는지
print(max)
