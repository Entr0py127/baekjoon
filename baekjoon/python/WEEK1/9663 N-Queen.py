n=int(input())
map=[0]*n
cnt=0

def check(x,y):
    for i in range(x):
        if(map[i]==y): #같은 열
            return False
        if(abs(x-i)==abs(map[i]-y)):
            return False
    return True

def put(a):     #a번째 줄에
    global cnt
    if a>=n:
        cnt+=1
        return
    for i in range(n):  #0~n-1 까지 다 넣어보고
        if check(a,i):  #만약 넣을 수 있으면
            map[a]=i #넣고 다음줄
            put(a+1)
put(0)
print(cnt)
