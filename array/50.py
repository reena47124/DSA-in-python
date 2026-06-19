#array
#replace with adjacent multiplication,optimise approach.
def adj_mul(a):
    n=len(a)
    a[0]=1*a[0]*a[1]
    prev=a[0]
    for i in range(1,n-1):
        curr=a[i]
        a[i]=prev*a[i]*a[i+1]
        prev=curr
    a[n-1]=prev*a[n-1]*1
    return a
a=[1,2,3,4,5]
print(adj_mul(a))
