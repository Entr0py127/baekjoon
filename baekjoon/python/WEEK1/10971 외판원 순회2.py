def move(num,location,start):#순회한 갯수 n, 현재 위치location
    global cost_sum,min_cost
    if num==n:
        if (cost[location][start])&(cost_sum+cost[location][start]<min_cost):
            min_cost=cost_sum+cost[location][start]
        return

    for i in range(n):
        if (not visited[i])&(not cost[location][i]==0)&(cost_sum+cost[location][i]<min_cost):
            visited[i]=True
            cost_sum += cost[location][i]
            move(num+1,i,start)
            cost_sum -= cost[location][i]
            visited[i]=False

n = int(input())
cost=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    cost[i]=list(map(int,input().split()))
cost_sum=0
min_cost=10**7
visited=[False]*n
for i in range(n):
    visited[i]=True
    move(1,i,i)
    visited[i] = False
print(min_cost)

