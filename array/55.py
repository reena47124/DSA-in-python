#array
#reverse the array in group,optimise method.
def rev_array(a,k):
    n=len(a)
    for i in range(0,n,k):
        left=i
        right=min(i+k-1,n-1)
        while left<=right:
            a[left],a[right]=a[right],a[left]
            left+=1
            right-=1
    return a
a=[1,2,3,4,5,6,7,8]
k=3
print(rev_array(a,k))        