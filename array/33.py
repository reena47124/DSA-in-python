#array
#delete an element from an array,from the begining,using custom method
a=[2,4,6,8,10]
n=len(a)
print("array before deletion:",end="")
for i in range(n):
    print(a[i],end=" ")
print()
for i in range(1,n):
    a[i-1]=a[i]
n=n-1
print("array after deletion:",end=" ")
for i in range(n):
    print(a[i],end=" ")
            