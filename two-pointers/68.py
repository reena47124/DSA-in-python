#two-pointers
#sum of pair equal to target,two-pointer approach,optimize approach
def two_sum(a,target):
    n=len(a)
    left=0
    right=n-1
    while left<right:
        sum=a[left]+a[right]
        if sum==target:
            print(a[left],a[right])
            return True
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
    return False
a=[-3,-1,0,1,2]
target=-2
if two_sum(a,target):
    print("true")
else:
    print("false")                