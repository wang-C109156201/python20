s="0123456"
print(s[1:3])
p=input("請輸入正整數:")
d=t=0
for i in range(len(p),0,-1):
    for j in range(0,i):
        r=int(p[j:i])
        print(r)
        d=0
        for k in range(2,r):
            if r%k==0:
                d+=1
        if d==0:
            if r>t:
                t=r
if t!=0:
    print("子字串中最大的質數值為:"+str(t))
else:
    print("子字串中最大的質數值為:No prime found")    
                    