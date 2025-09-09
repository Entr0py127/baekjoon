x,y =map(int,input().split())
line=int(input())
width=[]
height=[]
for _ in range(line):
    a,b=map(int,input().split())
    if a: #가로로 자름/ 숫자는 세로
        height.append(b)
    else: #세로
        width.append(b)
width.append(y)
width.append(0)
height.append(x)
height.append(0)
width.sort()
height.sort()
max=-100
for i in range(len(height)-1):
    for j in range(len(width)-1):
        area=(height[i+1]-height[i])*(width[j+1]-width[j])
        if(max<area):
            max=area
print(max)