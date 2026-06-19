#array
#check if an array is sorted or not,using recursion function.
def issorted(a,n):
    if(n==0 or n==1):
        return True
    return (a[n-1]>=a[n-2]) and issorted(a,n-1)
a=[1,3,4,6,8,9,56]
if issorted(a,len(a)):
    print("true")
else:
    print("false")    