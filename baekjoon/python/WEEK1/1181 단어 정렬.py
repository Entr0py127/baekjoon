n=int(input())
lst=[]

for _ in range(n):
    lst.append(input())
lst=list(set(lst))
lst.sort(key=lambda word: (len(word),word) )
for i in range(len(lst)):
    print(lst[i])