#sliding window
#maximum sum of subarray of size k.
def max_sum(a,k):
    n=len(a)
    window_sum=0
    for i in range(k):
        window_sum+=a[i]
    maxsum=window_sum
    for i in range(k,n):
        window_sum=window_sum-a[i-k]+a[i]
        if window_sum>maxsum:
            maxsum=window_sum
    return maxsum
a=[1,4,2,10,23,3,1,0,20]
k=4
print(max_sum(a,k))        