h=[]
sum=0
for i in range(9):
    h.append(int(input()))
    sum+=h[i]
for i in range(1,9):
    for j in range(i):
        if (sum-100)==h[i]+h[j]:
            del h[i]
            del h[j]
            h.sort()
            for i in range(7):
                print(h[i])
            quit()

