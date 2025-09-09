from math import ceil,floor
def make_number(a,d,n):
    arr=""
    for i in range(n):
        arr+=str(a+(i)*d)
    return int(arr)
n=int(input())
k=len(str(n))
cnt=0
cnt_1,cnt_2,cnt_3=0,0,0 #자리수k-1/자리수k 앞자리 1~n[0]-1/자리수k 앞자리 n[0]
first=int(str(n)[0])
for i in range(1, k):  # 자리수 i
     if i == 1:
         cnt_1 += 9
     else:
         for a in range(1, 10):  # 첫 앞자리 a
            cnt_1 += floor((9 - a) / (i - 1)) - ceil(-a / (i - 1)) + 1
if (k >= 2):
     for i in range(1, first):  # 앞자리 i(1~n[0]-1)
          cnt_2 += floor((9 - i) / (k - 1)) - ceil(-i / (k - 1)) + 1  # 끝자리 0 제외

else:
    cnt_2+=n
#앞자리 n[0]
if(k>=2):
  #  print(ceil(-first/(k-1)),floor((9-first)/(k-1)+1))
    for i in range(ceil(-first/(k-1)),floor((9-first)/(k-1)+1)):
        if make_number(first,i,k)<=n:
            cnt_3+=1

print(cnt_1+cnt_2+cnt_3)