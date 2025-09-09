a, b=map(int,input().split())
a_1=a%10
b_1=b%10
a_2=int(a/10)%10
b_2=int(b/10)%10
a_3=a//100
b_3=b//100
a_inv=a_1*100+a_2*10+a_3
b_inv=b_1*100+b_2*10+b_3
if(a_inv>b_inv):
    print(a_inv)
else:
    print(b_inv)