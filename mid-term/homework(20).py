p=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
s=input("輸入查詢學號為:")
if s==p[0][0]:
    print("學生資料為:"+str(p[0][0])+" "+str(p[0][1])+" "+str(p[0][2]))
elif s==p[1][0]:
    print("學生資料為:"+str(p[1][0])+" "+str(p[1][1])+" "+str(p[1][2]))
elif s==p[2][0]:
    print("學生資料為:"+str(p[2][0])+" "+str(p[2][1])+" "+str(p[2][2]))
elif s==p[3][0]:
    print("學生資料為:"+str(p[3][0])+" "+str(p[3][1])+" "+str(p[3][2]))          
else:
    print("學生資料為:"+str(p[4][0])+" "+str(p[4][1])+" "+str(p[4][2]))  
