a=input().split(" ")
dict={"A":14,"J":11,"Q":12,"K":13,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
b=0
for i in a:
    c=dict.get(i)
    b+=int(c)
    c=0
print(b)    