a=int(input("輸入第一行正整數:"))
b=input("第二行數列中的數字為:").split(" ")
t=n=d=0
c=[]
while len(b)!=a:
    a=int(input("輸入第一行正整數:"))
    b=input("第二行數列中的數字為:").split(" ")
for i in b:
    n=b.count(i) 
    if n>1:
        c.append(i)
        if n>t:
            t=n
            print(t)
if t!=0:
    d=max(c)
    print(c)
    print("出現次數為"+str(t))
    print("最大出現次數的數字為:"+str(d))
else:
    print("每個數字都只出現1次")   