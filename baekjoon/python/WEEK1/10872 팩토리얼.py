def function(num,start,goto):
        if(num==0):
            return
        empty=6-start-goto
        function(num-1,start,empty)
        print(start,goto)
        function(num-1,empty,goto)
n=int(input())
a=2**n-1
print(a)
if(n<=20):
    function(n,1,3)
