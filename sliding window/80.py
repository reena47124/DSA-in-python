#sliding window
#find maximum sum of a subarray with k elements,brute force approach.
def max_sum(a,k):
    n=len(a)
    maxsum=float('-inf')
    for i in range(n-k+1):
        cur_sum=0
        for j in range(i,i+k):
            cur_sum+=a[j]
        if cur_sum>maxsum:
            maxsum=cur_sum
    return maxsum
a=[5,2,-1,0,3]
k=3
print(max_sum(a,k))            