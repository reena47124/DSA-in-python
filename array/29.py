#array
#insert an element in an array,at a given position,using custom method.
a=[2,4,6,8,10]
pos=3
ele=100
print("array before insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
a.append(0)
for i in range(len(a)-1,pos-1,-1):
    a[i]=a[i-1]
a[pos-1]=ele 
print("array after insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
