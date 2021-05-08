a=input("輸入一組四位數字為:")
b=0
c=[]
for i in a:
    b=(int(i)+7)%10
    c.append(b)
   
tmp=""
tmp=c[2]
c[2]=c[0]
c[0]=tmp

tmp=""
tmp=c[3]
c[3]=c[1]
c[1]=tmp

d=""
for i in c:
    d+=str(i)
print("輸出加密後的數字為:"+str(d))