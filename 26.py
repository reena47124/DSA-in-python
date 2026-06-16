#array
#insert element in an array,at the beginning,bult-in method
a=[2,4,6,8,10]
ele=0
print("array before insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()    
a.insert(0,ele)
print("array after insertion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
