#array
#insert element in an array,at the beginning,using custom method
a=[2,4,6,8,10]
ele=0
n=len(a)
print("array before insertion:",end="")
for i in range(n):
    print(a[i],end=" ")
print() 
a.append(0)           #creating extra space
for i in range(n-1,-1,-1):
    a[i+1]=a[i]
a[0]=ele
print("array after insertion:",end="")
for i in range(n+1):
    print(a[i],end=" ")       