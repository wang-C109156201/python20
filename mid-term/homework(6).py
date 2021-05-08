p=input("輸入值為:").split(",")
p=sorted(p,reverse=True)
print(p)
w=""
for i in p:
    w+=str(i)
a=int(w)

p.sort()#小到大
print(p)

y=""
for i in p:
    y+=str(i)
b=int(y)
print(a-b)  

