#array
#remove all occurrences of an element from an array,using built-in method.
a=[1,2,2,3,2,4,5]
ele=2
b=[]
print("array before deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()    
for i in range(len(a)):
    if a[i]!=ele:
        b.append(a[i])
print("array after deletion",end="")
for i in range(len(b)):
    print(b[i],end=" ")        