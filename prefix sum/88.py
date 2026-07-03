#prefix sum
#find prefix sum of given array.
a=[2,4,6,8,10]
n=len(a)
prefix=[0]*n
prefix[0]=a[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+a[i]
print(prefix)    