a=input("輸入一整數序列為:").split(" ")
c=[]
for i in a:
    b=0
    b=a.count(i)
    if b>(len(a)/2):
        c.append(i)
if c!=[]:
    print("過半元素為:"+str(c[0]))
else:
    print("過半元素為:NO")    
