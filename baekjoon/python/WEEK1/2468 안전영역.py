import sys
sys.setrecursionlimit(10**6)
def get_area_num(rain):
    area_num=0
    for i in range(n):
        for j in range(n):
            if(height[i][j]<=rain):
                water[i][j]=True
    for i in range(n):
        for j in range(n):
            if not water[i][j]:
                area_num+=1
                color(i,j)
    return area_num
def color(c,r):
    water[c][r]=True
    if((c-1>=0)and(not water[c-1][r])):
        color(c-1,r)
    if((r-1>=0)and(not water[c][r-1])):
        color(c,r-1)
    if((c+1<n)and(not water[c+1][r])):
        color(c+1,r)
    if((r+1<n)and(not water[c][r+1])):
        color(c,r+1)
n = int(input())
height=[[0 for _ in range(n)] for _ in range(n)]
max_height=-1
for i in range(n):
    height[i]=list(map(int,input().split()))
    a=max(height[i])
    if(a>max_height):
        max_height=a
num_area=[-1]*max_height
for i in range(max_height):
    water = [[False for _ in range(n)] for _ in range(n)]
    num_area[i]=get_area_num(i)

print(max(num_area))