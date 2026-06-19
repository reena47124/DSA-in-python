#array
#reverse an in a group,using extend method.
def rev_array(a,k):
    n=len(a)
    b=[]
    for i in range(0,n,k):
        b.extend(a[i:i+k][::-1])
    return b
a=[1,2,3,4,5,6,7,8]
k=3
print(rev_array(a,k))

