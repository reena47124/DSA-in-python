#array
#insert an element in an array,at the end,using custom method
a=[2,4,6,8,10,0]
ele=99
print("array before insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
a[len(a)-1]=ele
print("array after insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
