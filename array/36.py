#array
#delete first occurence of the giving element from an array,using custom method.
a=[1,2,2,3,4,5]
ele=2
n=len(a)
print("array before deletion:",end="")
for i in range(n):
    print(a[i],end=" ")
print()
found=False
for i in range(n):
    if found:
        a[i-1]=a[i]
    elif a[i]==ele:
        found=True
if found:
    n=n-1
print("array after deletion",end=" ")
for i in range(n):
    print(a[i],end=" ")

