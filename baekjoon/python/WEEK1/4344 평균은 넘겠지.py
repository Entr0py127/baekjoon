c=int(input())
for _ in range(c):
    score=list(map(int,input().split()))
    sum=0
    over_avg=0
    for i in range(1,score[0]+1):
        sum+=score[i]
    avg=sum/score[0]
    for i in range(1,score[0]+1):
        if score[i]>avg:
            over_avg+=1
    print("%.3f%%"%(over_avg*100/score[0]))
