#prefix sum
#equilibrium index,better approach,prefix sum and suffix sum.
def equi_index(a):
    n=len(a)
    prefix=[0]*n
    prefix[0]=a[0]
    suffix=[0]*n
    suffix[n-1]=a[n-1]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+a[i]
    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]+a[i]
    for i in range(n):
        if prefix[i]==suffix[i]:
            return i
    return -1
a=[1,1,1,1]
print(equi_index(a))
b=[-7,1,5,2,-4,3,0]
print(equi_index(b))            
