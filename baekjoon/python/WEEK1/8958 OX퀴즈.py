n=int(input())
score_total=0
for _ in range(n):
    #print(score_total)
    arr=list(input())
    score=1
    score_total=0
    for i in range(len(arr)):
        #print(arr[i],end='')
        if arr[i]=='O':
            score_total+=score
            score+=1
            #print(score)
        else:
            score=1
            #print(score)
    print(score_total)
