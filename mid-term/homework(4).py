x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
c=(x*x)+(y*y)
if x>0 and y>0:
    print("第一象限,離原點距離為根號"+str(c))
elif x<0 and y>0:
    print("第二象限,離原點距離為根號"+str(c)) 
elif x<0 and y<0:
    print("第三象限,離原點距離為根號"+str(c))         
elif x>0 and y<0:
    print("第四象限,離原點距離為根號"+str(c))    
elif x==0 and y>0:
    print("該點位於上半平面Y軸上,離原點距離為根號"+str(c)) 
elif x==0 and y<0:
    print("該點位於下半平面Y軸上,離原點距離為根號"+str(c)) 
elif x>0 and y==0:
    print("該點位於右半平面X軸上,離原點距離為根號"+str(c)) 
elif x<0 and y==0:
    print("該點位於左半平面X軸上,離原點距離為根號"+str(c)) 
else:
    print("位於原點")    