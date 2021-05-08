a=input().split(" ")
b=input().split(" ")
c=input().split(" ")
a2=input().split(" ")
b2=input().split(" ")
c2=input().split(" ")
e=f=g=h=0
if a!=a2:
    print("兩個矩陣無法相加") 
else:
    e=int(b[0])+int(b2[0])
    f=int(b[1])+int(b2[1])
    g=int(c[0])+int(c2[0])
    h=int(c[1])+int(c2[1])
    print(e,f)
    print(g,h)