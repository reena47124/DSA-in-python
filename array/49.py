#array
#replace with adjacent multiplication,function method
def adj_mul(a):
    n=len(a)
    b=[]
    for i in range(n):
        if i==0:
            b.append(1*a[i]*a[i+1])
        elif i==(n-1):
            b.append(a[i-1]*a[i]*1)
        else:
            b.append(a[i-1]*a[i]*a[i+1])
    return b 
a=[1,2,3,4,5]
print(adj_mul(a))
