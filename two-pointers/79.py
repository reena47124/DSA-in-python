#two-pointer
#dutch national flag problem,two-pointer technique
def func_dutch(a):
    n=len(a)
    lo=0
    mid=0
    hi=n-1
    while mid<=hi:
        if a[mid]==0:
            a[lo],a[mid]=a[mid],a[lo]
            lo+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[hi]=a[hi],a[mid]
            hi-=1
    return a
a=[1,2,1,0,0,2,1,0]
print(func_dutch(a))                