#array
##delete an element from the end of an array,using custom method.
a=[1,2,3,4,5,6,7]
n=len(a)
print("array before deletion:",end="")
for i in range(n):
    print(a[i],end=" ")
print()
n-=1
print("array after deletion:",end="")
for i in range(n):
    print(a[i],end=" ")