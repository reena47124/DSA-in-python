#array
#insert element in an array,at a given position,using built-in method
a=[2,4,6,8,10]
pos=3
ele=100
print("array before insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
a.insert(pos-1,ele)
print("array after insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
        