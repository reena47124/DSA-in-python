#two pointers
#sum of pair equal to target,using function.
def two_sum(a,target):
    n=len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j]==target:
                print(a[i],a[j])
                return True
    return False
a=[10,20,35,50]
target=70
if two_sum(a,target):
    print("true")
else:
    print("false")    
        