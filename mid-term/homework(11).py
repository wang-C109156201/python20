a=input("輸入月及日為:").split(" ")
p=["Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
if a[0]=="1":
    if int(a[1])>=21:
        print("星座為:"+str(p[0]))
    else:
        print("星座為:"+str(p[11]))
elif a[0]=="2":
    if int(a[1])>=19:
        print("星座為:"+str(p[1]))
    else:
        print("星座為:"+str(p[0]))
elif a[0]=="3":
    if int(a[1])>=21:
        print("星座為:"+str(p[2]))        
    else:
        print("星座為:"+str(p[1]))
elif a[0]=="4": 
    if int(a[1])>=21:
        print("星座為:"+str(p[3]))       
    else:
        print("星座為:"+str(p[2]))
elif a[0]=="5":
    if int(a[1])>=22:
        print("星座為:"+str(p[4]))
    else:
        print("星座為:"+str(p[3]))
elif a[0]=="6":
    if int(a[1])>=22:
        print("星座為:"+str(p[5]))        
    else:
        print("星座為:"+str(p[4]))
elif a[0]=="7":
    if int(a[1])>=23:
        print("星座為:"+str(p[6]))        
    else:
        print("星座為:"+str(p[5]))
elif a[0]=="8":
    if int(a[1])>=24:
        print("星座為:"+str(p[7]))        
    else:
        print("星座為:"+str(p[6])) 
elif a[0]=="9":
    if int(a[1])>=24:
        print("星座為:"+str(p[8]))        
    else:
        print("星座為:"+str(p[7]))
elif a[0]=="10":
    if int(a[1])>=24:
        print("星座為:"+str(p[9]))        
    else:
        print("星座為:"+str(p[8]))  
elif a[0]=="11":
    if int(a[1])>=23:
        print("星座為:"+str(p[10]))        
    else:
        print("星座為:"+str(p[9]))
else:
    if int(a[1])>=22:
        print("星座為:"+str(p[11]))        
    else:
        print("星座為:"+str(p[10]))                                                                         
