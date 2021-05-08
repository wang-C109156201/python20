m=input("輸入值為:").split(",")
a=0
b=0
if m[0]=="186":
    a=int(m[1])
    if 186<a<=186*2:
        b=a*0.09*0.9
    else:
        b=a*0.09*0.8    
    print("通話費為:%d" %(b))
elif m[0]=="386":  
    a=int(m[1])
    if 386<a<=386*2:
        b=a*0.08*0.8
    else:
        b=a*0.08*0.7    
    print("通話費為:%d" %(b))
elif m[0]=="586":  
    a=int(m[1])
    if 586<a<=586*2:
        b=a*0.07*0.7
    else:
        b=a*0.07*0.6    
    print("通話費為:"+str(b))
else:  
    a=int(m[1])
    if 986<a<=986*2:
        b=a*0.06*0.6
    else:
        b=a*0.06*0.5    
    print("通話費為:"+str(b))        
