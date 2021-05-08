d=int(input("度數:"))
s=uns=0
if d<=120:
    s+=d*2.10
    uns+=d*2.10
else:
    s+=120*2.10
    uns+=120*2.10
    if d<=330:
        s+=(d-120)*3.02
        uns+=(d-120)*2.68
    else:
        s+=210*3.02
        uns+=210*2.68
        if d<=500:
            s+=(d-330)*4.39
            uns+=(d-330)*3.61
        else:
            s+=170*4.39
            uns+=170*3.61
            if d<=700:
                s+=(d-500)*4.97
                uns+=(d-500)*4.01
            else:
                s+=200*4.97
                uns+=200*4.01
                if d>700:
                    s+=(d-700)*5.63
                    uns+=(d-700)*4.50
    

                    

print("Summer months:"+str(s))
print("Non-Summer months:"+str(uns))