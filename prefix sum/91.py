#prefix sum
#subarray with sum zero,naive approach
def subarray_zero(a):
    n=len(a)
    for i in range(n):
        sum=a[i]
        if sum==0:
            return True
        for j in range(i+1,n):
            sum+=a[j]
            if sum==0:
                return True
    return False
a=[4,2,-3,1,6]
print(subarray_zero(a))
b=[-3,2,3,1,6]
print(subarray_zero(b))        