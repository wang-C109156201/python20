a=input("輸入N及M為:").split(" ")
b=[]

for i in range(1,int(a[0])+1):
    b.append(input("輸入矩陣數值第"+str(i)+"列為:").split(" "))
    print(b)
for y in range(0,int(a[1])):
    s=[]
    for x in range(0,int(a[0])):
        s.append(b[x][y])
    print("輸出矩陣數值第一列為:"+str(s))