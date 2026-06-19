#array
#replace with adjacent multiplication,naive approach
a=[1,2,3,4,5]
n=len(a)
b=[]
for i in range(len(a)):
    if i==0:
        b.append(1*a[i]*a[i+1])
    elif i==(n-1):
        b.append(a[i-1]*a[i]*1)
    else:
        b.append(a[i-1]*a[i]*a[i+1])
print("resultant array:",end="")
for i in range(len(b)):
    print(b[i],end=" ")

