m=int(input("請輸入階乘值M:"))
n=1
i=1
while n<=m:
    i+=1
    n*=i
    
print("超過M為"+str(m)+"的最小階層N值為:"+str(i))