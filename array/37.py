#array
#remove all occurrences of an element in an array,using custom method
a=[1,2,2,3,2,4,5]
ele=2
n=len(a)
print("array before deletion:",end="")
for i in range(n):
    print(a[i],end=" ")
print()
j=0
while j<n:
    found=False
    for i in range(n):
        if found:
            a[i-1]=a[i]
        elif a[i]==ele:
            found=True
    if found:
        n=n-1
    j+=1
print("array after deletion:",end="")
for i in range(n):
    print(a[i],end=" ")
