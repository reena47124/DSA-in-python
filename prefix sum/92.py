#prefix sum 
#subarray with sum zero,using hashing and prefix sum.
def subarray_zero(a):
    n=len(a)
    sumset=set()
    sum=0
    for i in range(n):
        sum+=a[i]
        if sum==0 or sum in sumset:
            return True
        sumset.add(sum)
    return False
a=[-3,2,3,1,6]
print(subarray_zero(a)) 
b=[1,4,-2,-2,5,-4,3]
print(subarray_zero(b))   
