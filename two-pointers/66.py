#two pointers
#sum of pair equal to target,naive approach.
a=[10,20,35,50]
target=70
n=len(a)
found=False
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
            found=True
            print(a[i],a[j])
if found:
    print("true")
else:
    print("false")                