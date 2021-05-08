a=int(input("組數為:"))
for i in range(1,a+1):
    b=input("第"+str(i)+"組:").split(" ")
    c=0
    c=int(b[0])*250+int(b[1])*175
    print("第"+str(i)+"組應收費用:"+str(c))