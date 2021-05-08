a=int(input("測試的資料量:"))

for i in range(1,a+1):
    b=input().split(" ")
    if b[0]=="O" and b[1]=="O" and b[2]=="O":
        print("YES")
    elif b[0]=="O" and b[1]=="A" and(b[2]=="O" or b[2]=="A"):
        print("YES")
    elif b[0]=="O" and b[1]=="B" and(b[2]=="O" or b[2]=="B"):
        print("YES")
    elif b[0]=="O" and b[1]=="AB" and(b[2]=="A" or b[2]=="B"):
        print("YES")
    elif b[0]=="A" and b[1]=="A" and(b[2]=="O" or b[2]=="A"):
        print("YES")
    elif b[0]=="B" and b[1]=="A" and(b[2]=="O" or b[2]=="A" or b[2]=="B" or b[2]=="AB"):
        print("YES")
    elif b[0]=="A" and b[1]=="AB" and(b[2]=="B" or b[2]=="A" or b[2]=="AB"):
        print("YES")
    elif b[0]=="B" and b[1]=="B" and(b[2]=="B" or b[2]=="O"):
        print("YES")
    elif b[0]=="B" and b[1]=="AB" and(b[2]=="B" or b[2]=="A" or b[2]=="AB"):
        print("YES")
    elif b[0]=="AB" and b[1]=="AB" and(b[2]=="B" or b[2]=="A" or b[2]=="AB"):
        print("YES")                                     
    else:
        print("IMPOSSIBLE")     